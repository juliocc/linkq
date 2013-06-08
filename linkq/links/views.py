import datetime

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView, FormView, ListView, View

import lxml.html
from braces.views import JSONResponseMixin, SetHeadlineMixin

from .models import Link
from .forms import NextLinkForm, AddLinkForm

class NextLinkView(UpdateView):
    context_objext_name = 'link'
    form_class = NextLinkForm
    template_name = 'links/next.html'
    fields = ['summary']
    model = Link
    success_url = reverse_lazy('index')

    def get_object(self, *args, **kwargs):
        l = list(Link.objects_unread.all()[:1])
        if l:
            return l[0]
        return None

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.read = datetime.datetime.now()
        return super(NextLinkView, self).form_valid(form)


class AddLinkView(FormView):
    form_class = AddLinkForm
    template_name = 'links/add.html'
    success_url = reverse_lazy('index')

    def get_candidate_title(self, url):
        try:
            e = lxml.html.parse(url).getroot()
            title = e.find('.//title')
            return title.text
        except:
            return None


    def form_valid(self, form):
        for url in form.cleaned_data['urls']:
            link, created = Link.objects.get_or_create(url=url)
            if created:
                msg = "Added {}".format(url)
                title = self.get_candidate_title(url)
                if title is not None:
                    link.title = title
                    link.save()
                messages.success(self.request, msg)
            else:
                msg = "You already have or had {} in your queue".format(url)
                messages.warning(self.request, msg)

        return super(AddLinkView, self).form_valid(form)


class QueuedLinksView(SetHeadlineMixin, ListView):
    queryset = Link.objects_unread.all()
    paginate_by = 10
    headline = 'Queued links'

class ReadLinksView(SetHeadlineMixin, ListView):
    queryset = Link.objects_read.all().order_by('-read')
    paginate_by = 5
    headline = 'Read links'


class CandidateTitleView(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        url = request.GET.get('url')
        title = self.get_candidate_title(url)
        return self.render_json_response({'title': title})



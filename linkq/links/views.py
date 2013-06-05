import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView, FormView, ListView
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

    def form_valid(self, form):
        for url in form.cleaned_data['urls']:
            link, created = Link.objects.get_or_create(url=url)
            if created:
                msg = "Added {}".format(url)
                messages.success(self.request, msg)
            else:
                msg = "You already have or had {} in your queue".format(url)
                messages.warning(self.request, msg)

        return super(AddLinkView, self).form_valid(form)

class ExtraContextMixin(object):
    extra_context = {}
    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context

class QueuedLinksView(ExtraContextMixin, ListView):
    queryset = Link.objects_unread.all()
    paginate_by = 10
    extra_context = {'title': 'Queued links'}

class ReadLinksView(ExtraContextMixin, ListView):
    queryset = Link.objects_read.all().order_by('-read')
    paginate_by = 5
    extra_context = {'title': 'Read links'}

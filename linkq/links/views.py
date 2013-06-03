import datetime
from django.views.generic import UpdateView
from .models import Link
from .forms import NextLinkForm

class NextLinkView(UpdateView):
    context_objext_name = 'link'
    form_class = NextLinkForm
    template_name = 'links/next.html'
    fields = ['summary']
    model = Link
    success_url = 'index'

    def get_object(self, *args, **kwargs):
        l = list(Link.objects_unread.all()[:1])
        if l:
            return l[0]
        return None

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.read = datetime.datetime.now()
        return super(NextLinkView, self).form_valid(form)


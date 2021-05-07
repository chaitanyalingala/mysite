from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad

class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['prize', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['prize', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
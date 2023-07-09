from django.db.models import Count, Prefetch
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from watches.models import Brand, Designer, Store, Watch


def index(request):
    """Renders the index page"""
    return render(request, "index.html")


class DesignerListView(ListView):
    model = Designer
    template_name = "designer_list.html"
    queryset = Designer.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of designers to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Designer.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class DesignerDetailView(DetailView):
    model = Designer
    template_name = "designer_detail.html"
    queryset = Designer.objects.prefetch_related("watch_set__brand")

    def get_context_data(self, **kwargs) -> dict:
        """Adds related watch brands to the context"""
        context = super().get_context_data(**kwargs)
        related_brands = self.object.watch_set.values("brand__name", "brand__pk").annotate(count=Count("brand__name"))
        context["related_brands"] = related_brands
        return context


class BrandListView(ListView):
    model = Designer
    template_name = "brand_list.html"
    queryset = Brand.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of brands to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Brand.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = "brand_detail.html"
    queryset = Brand.objects.prefetch_related(
        "watch_set__designer",
        Prefetch("watch_set__store_set", queryset=Store.objects.only("name", "pk")),
    )

    def get_context_data(self, **kwargs) -> dict:
        """Adds related watches and stores to the context"""
        context = super().get_context_data(**kwargs)
        brand = self.object
        related_watches = brand.watch_set.all()
        related_stores = (
            Store.objects.filter(watches__brand=brand).values("name", "pk").annotate(watch_count=Count("watches"))
        )
        context["related_watches"] = related_watches
        context["related_stores"] = related_stores
        return context


class WatchListView(ListView):
    model = Watch
    template_name = "watch_list.html"
    queryset = Watch.objects.select_related("brand")

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of watches to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Watch.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class WatchDetailView(DetailView):
    model = Watch
    template_name = "watch_detail.html"
    queryset = Watch.objects.select_related("brand", "designer").prefetch_related("store_set")


class StoreListView(ListView):
    model = Store
    template_name = "store_list.html"
    queryset = Store.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of stores to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Store.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class StoreDetailView(DetailView):
    model = Store
    template_name = "store_detail.html"

    def get_context_data(self, **kwargs) -> dict:
        """Adds related brands to the context"""
        context = super().get_context_data(**kwargs)
        context["brands"] = self.object.watches.values("brand__name", "brand__pk").annotate(count=Count("brand__name"))
        return context

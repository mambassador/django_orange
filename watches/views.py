from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Prefetch
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from watches.models import Brand, Designer, Store, Watch


def index(request):
    """Renders the index page"""
    return render(request, "watches/index.html")


class DesignerListView(generic.ListView):
    paginate_by = 12
    model = Designer
    template_name = "watches/designer_list.html"
    queryset = Designer.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of designers to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Designer.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class DesignerDetailView(generic.DetailView):
    model = Designer
    template_name = "watches/designer_detail.html"
    queryset = Designer.objects.prefetch_related("watch_set__brand")

    def get_context_data(self, **kwargs) -> dict:
        """Adds related watch brands to the context"""
        context = super().get_context_data(**kwargs)
        related_brands = self.object.watch_set.values("brand__name", "brand__pk").annotate(count=Count("brand__name"))
        context["related_brands"] = related_brands
        return context


class BrandListView(generic.ListView):
    paginate_by = 12
    model = Designer
    template_name = "watches/brand_list.html"
    queryset = Brand.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of brands to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Brand.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = "watches/brand_detail.html"
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


class WatchListView(generic.ListView):
    paginate_by = 12
    model = Watch
    template_name = "watches/watch_list.html"
    queryset = Watch.objects.select_related("brand").order_by("-pk")

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of watches to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Watch.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class WatchDetailView(generic.DetailView):
    model = Watch
    template_name = "watches/watch_detail.html"
    queryset = Watch.objects.select_related("brand", "designer").prefetch_related("store_set")


class WatchCreateView(LoginRequiredMixin, generic.CreateView):
    model = Watch
    template_name_suffix = "_create_form"
    fields = ["name", "price", "designer", "brand", "colour", "size"]
    success_url = reverse_lazy("watches:watches")


class WatchUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Watch
    template_name_suffix = "_update_form"
    fields = ["name", "price", "designer", "brand", "colour", "size"]

    def get_success_url(self):
        watch_pk = self.object.pk
        return reverse_lazy("watches:watch-detail", kwargs={"pk": watch_pk})


class WatchDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Watch
    success_url = reverse_lazy("watches:watches")


class StoreListView(generic.ListView):
    paginate_by = 12
    model = Store
    template_name = "watches/store_list.html"
    queryset = Store.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        """Adds the total count of stores to the context"""
        context = super().get_context_data(**kwargs)
        context["total_count"] = Store.objects.aggregate(total_count=Count("id"))["total_count"]
        return context


class StoreDetailView(generic.DetailView):
    model = Store
    template_name = "watches/store_detail.html"

    def get_context_data(self, **kwargs) -> dict:
        """Adds related brands to the context"""
        context = super().get_context_data(**kwargs)
        context["brands"] = self.object.watches.values("brand__name", "brand__pk").annotate(count=Count("brand__name"))
        return context

from repoze.catalog.query import Eq
from pyramid.url import resource_url
from w20e.pycms.views.base import ContentView
from w20e.pycms_events.interfaces import IEvent


class EventsListingMixin:
    
    def listevents(self):

        cat = self.context.root._catalog

        res = cat.query(Eq('nature', "w20e.pycms_events.interfaces.IEvent"))

        objs = []

        for result in res[1]:
            obj = cat.get_object(result)
            
            objs.append({"title": obj.title,
                         "date": obj.created.strftime('%d-%m-%Y'),
                         "sortdate": obj.created.strftime('%Y%m%d'),
                         "url": resource_url(obj, self.request),
                         "text": obj.full_text})

        def newest_sort(a, b):

            return cmp(b['sortdate'], a['sortdate'])

        objs.sort(newest_sort)
                
        return objs


class EventsViewlet(object, EventsListingMixin):

    """ Fetch events and provide to viewlet"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

        self.limit = self.request.get('kwargs', {}).get('limit', 5)
        self._events = self.listevents()

    def __call__(self):

        return {}

    @property
    def events(self):

        return self._events[:self.limit]

    @property
    def has_more_events(self):

        return len(self._events) > self.limit


class EventView(ContentView):

    @property
    def date(self):
        return self.context.created.strftime('%d-%m-%Y')


class EventsListingView(ContentView, EventsListingMixin):

    pass

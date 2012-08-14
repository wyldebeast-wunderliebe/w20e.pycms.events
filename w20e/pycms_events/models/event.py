from zope.interface import implements
from w20e.forms.interfaces import IForm, IFormModifier
from w20e.forms.data.field import Field
from w20e.forms.model.fieldproperties import FieldProperties
from w20e.forms.rendering.control import Input
from w20e.forms.rendering.group import FlowGroup


class Event(object):

    implements(IFormModifier)

    def __init__(self, form):

        self.form = form

    def modify(self, form):

        """ Add begin, end and location to form """

        #import pdb; pdb.set_trace()

        form.data.addField(Field("start"))
        form.data.addField(Field("end"))
        form.data.addField(Field("location"))

        #form.model.addFieldProperties(FieldProperties("datetime",
        #                                              ["start", "end"],
        #                                              datatype="datetime"))

        grp = FlowGroup("eventgroup", label="Event")
        grp.addRenderable(Input("start", "Start of event",
                                extra_classes="datetime",
                                bind="start"))
        grp.addRenderable(Input("end", "End of event", bind="end"))
        grp.addRenderable(Input("location", "Location", bind="location"))

        form.view.addRenderable(grp, pos=-1)

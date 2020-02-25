from django.shortcuts import render
from django.views.generic import TemplateView


class CategoryView(TemplateView):
    template_name = 'category/listCategory.html'

    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['event_id'])
        bracket_list = Bracket.objects.select_related('group').order_by('status').filter(
            status__in=['PLAY', 'PREPARE_FIRST', 'PREPARE_SECOND'],
            group__event_id=event.id
        )
        # print('bracket_list')
        # print(bracket_list)
        return render(request, self.template_name, context={
            'bracket_list': bracket_list,
            'event': event,
        })
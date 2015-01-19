# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.forms import NON_FIELD_ERRORS
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView
from django.views.generic.edit import ModelFormMixin

# Local application / specific library imports
from machina.core.db.models import get_model
from machina.core.loading import get_class
from machina.views.mixins import PermissionRequiredMixin

TopicPoll = get_model('polls', 'TopicPoll')
TopicPollVote = get_model('polls', 'TopicPollVote')

TopicPollVoteForm = get_class('polls.forms', 'TopicPollVoteForm')

PermissionHandler = get_class('permission.handler', 'PermissionHandler')
perm_handler = PermissionHandler()


class TopicPollVoteView(PermissionRequiredMixin, UpdateView):
    model = TopicPoll
    form_class = TopicPollVoteForm
    http_method_names = ['post', ]

    def get_form_kwargs(self):
        kwargs = super(ModelFormMixin, self).get_form_kwargs()
        kwargs['poll'] = self.object
        return kwargs

    def form_valid(self, form):
        if self.object.user_changes:
            # If user changes are allowed for this poll, all
            # the poll associated with the current user must
            # be deleted.
            TopicPollVote.objects.filter(
                poll_option__poll=self.object,
                voter=self.request.user).delete()

        options = form.cleaned_data['options']
        for option in options:
            if option.poll != self.object:
                return HttpResponseForbidden()
            TopicPollVote.objects.create(
                poll_option=option, voter=self.request.user)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors[NON_FIELD_ERRORS])
        return redirect(reverse('conversation:topic', kwargs={
            'forum_slug': self.object.topic.forum.slug,
            'forum_pk': self.object.topic.forum.pk,
            'slug': self.object.topic.slug,
            'pk': self.object.topic.pk}))

    def get_success_url(self):
        messages.success(self.request, _('Your vote has been cast.'))
        return reverse('conversation:topic', kwargs={
            'forum_slug': self.object.topic.forum.slug,
            'forum_pk': self.object.topic.forum.pk,
            'slug': self.object.topic.slug,
            'pk': self.object.topic.pk})

    # Permissions checks

    def get_controlled_object(self):
        """
        Returns the poll that will be answered.
        """
        return self.get_object()

    def perform_permissions_check(self, user, obj, perms):
        return perm_handler.can_vote_in_poll(obj, user)

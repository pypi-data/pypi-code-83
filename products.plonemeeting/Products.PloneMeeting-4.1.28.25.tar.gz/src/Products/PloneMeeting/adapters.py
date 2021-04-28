# -*- coding: utf-8 -*-
#
# File: adapters.py
#

from appy.shared.diff import HtmlDiff
from collective.contact.plonegroup.utils import get_own_organization
from collective.contact.plonegroup.utils import get_plone_group_id
from collective.documentgenerator.adapters import GenerablePODTemplatesAdapter
from collective.documentgenerator.content.pod_template import IPODTemplate
from collective.eeafaceted.dashboard.adapters import DashboardGenerablePODTemplatesAdapter
from collective.eeafaceted.dashboard.content.pod_template import IDashboardPODTemplate
from collective.iconifiedcategory.adapter import CategorizedObjectAdapter
from collective.iconifiedcategory.adapter import CategorizedObjectInfoAdapter
from collective.iconifiedcategory.utils import get_categories
from DateTime import DateTime
from datetime import datetime
from eea.facetednavigation.criteria.handler import Criteria as eeaCriteria
from eea.facetednavigation.interfaces import IFacetedNavigable
from eea.facetednavigation.widgets.resultsperpage.widget import Widget as ResultsPerPageWidget
from eea.facetednavigation.widgets.storage import Criterion
from imio.actionspanel.adapters import ContentDeletableAdapter as APContentDeletableAdapter
from imio.annex.adapters import AnnexPrettyLinkAdapter
from imio.helpers.catalog import merge_queries
from imio.helpers.xhtml import xhtmlContentIsEmpty
from imio.history.adapters import BaseImioHistoryAdapter
from imio.history.adapters import ImioWfHistoryAdapter
from imio.prettylink.adapters import PrettyLinkAdapter
from persistent.list import PersistentList
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.querystring.queryparser import parseFormquery
from plone.memoize import ram
from plone.memoize.instance import memoize
from Products.CMFCore.permissions import AccessContentsInformation
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import _checkPermission
from Products.CMFPlone.utils import safe_unicode
from Products.PloneMeeting.config import AddAnnexDecision
from Products.PloneMeeting.config import DUPLICATE_AND_KEEP_LINK_EVENT_ACTION
from Products.PloneMeeting.config import DUPLICATE_EVENT_ACTION
from Products.PloneMeeting.config import EMPTY_STRING
from Products.PloneMeeting.config import HIDDEN_DURING_REDACTION_ADVICE_VALUE
from Products.PloneMeeting.config import ITEM_NO_PREFERRED_MEETING_VALUE
from Products.PloneMeeting.config import MEETINGROLES
from Products.PloneMeeting.config import NOT_GIVEN_ADVICE_VALUE
from Products.PloneMeeting.config import READER_USECASES
from Products.PloneMeeting.interfaces import IMeeting
from Products.PloneMeeting.MeetingConfig import CONFIGGROUPPREFIX
from Products.PloneMeeting.MeetingConfig import PROPOSINGGROUPPREFIX
from Products.PloneMeeting.MeetingConfig import READERPREFIX
from Products.PloneMeeting.MeetingConfig import SUFFIXPROFILEPREFIX
from Products.PloneMeeting.utils import displaying_available_items
from Products.PloneMeeting.utils import findNewValue
from Products.PloneMeeting.utils import getCurrentMeetingObject
from Products.PloneMeeting.utils import getHistoryTexts
from Products.PloneMeeting.utils import reviewersFor
from zope.annotation import IAnnotations
from zope.i18n import translate

import logging


logger = logging.getLogger('PloneMeeting')


# this catalog query will find nothing, used in CompoundCriterion adapters when necessary
def _find_nothing_query(portal_type):
    """ """
    query = {'UID': {'query': 'dummy_unexisting_uid'}, }
    return query


class AnnexContentDeletableAdapter(APContentDeletableAdapter):
    """
      Manage the mayDelete for annex and annexDecision.
      An annex/annexDecision can be deleted by users able to edit parent (item or advice).
      An annexDecision is deletable by the annexDecision Owner still able to add annexDecision.
    """
    def __init__(self, context):
        self.context = context

    def mayDelete(self, **kwargs):
        '''See docstring in interfaces.py.'''
        # check 'Delete objects' permission
        mayDelete = super(AnnexContentDeletableAdapter, self).mayDelete()
        if not mayDelete:
            parent = self.context.getParentNode()
            # able to delete an annex/annexDecision if able to edit the parent
            if _checkPermission(ModifyPortalContent, parent):
                return True

            # a 'Owner' may still remove an 'annexDecision' if enabled
            # in the cfg and if still able to add 'annexDecision'
            elif self.context.portal_type == 'annexDecision':
                tool = api.portal.get_tool('portal_plonemeeting')
                cfg = tool.getMeetingConfig(self.context)
                if cfg.getOwnerMayDeleteAnnexDecision() and \
                   _checkPermission(AddAnnexDecision, parent):
                    member = api.user.get_current()
                    if 'Owner' in member.getRolesInContext(self.context):
                        return True
        return mayDelete


class AdviceContentDeletableAdapter(APContentDeletableAdapter):
    """
      Manage the mayDelete for meetingadvice.
      Must have 'Delete objects' on the item.
      If some versions are saved (advice was asked_again at least once), advice
      is not deletable.
    """
    def __init__(self, context):
        self.context = context

    def mayDelete(self, **kwargs):
        '''See docstring in interfaces.py.'''
        # check 'Delete objects' permission
        mayDelete = super(AdviceContentDeletableAdapter, self).mayDelete()
        if mayDelete:
            tool = api.portal.get_tool('portal_plonemeeting')
            pr = api.portal.get_tool('portal_repository')
            if not tool.isManager(self.context, realManagers=True) and \
               pr.getHistoryMetadata(self.context):
                return False
        return mayDelete


class MeetingItemContentDeletableAdapter(APContentDeletableAdapter):
    """
      Manage the mayDelete for MeetingItem.
      Must have 'Delete objects' on the item.
    """
    def __init__(self, context):
        self.context = context

    def mayDelete(self, **kwargs):
        '''See docstring in interfaces.py.'''
        # check 'Delete objects' permission
        mayDelete = super(MeetingItemContentDeletableAdapter, self).mayDelete()
        if mayDelete:
            # check itemWithGivenAdviceIsNotDeletable
            tool = api.portal.get_tool('portal_plonemeeting')
            cfg = tool.getMeetingConfig(self.context)
            if cfg.getItemWithGivenAdviceIsNotDeletable() and not tool.isManager(self.context):
                # do we have any given advice?
                # do not consider advices that are inherited
                given_advices = [advice for advice in self.context.adviceIndex.values() if
                                 not advice['inherited'] and not advice['type'] == NOT_GIVEN_ADVICE_VALUE]
                if given_advices:
                    return False
        return mayDelete


class MeetingContentDeletableAdapter(APContentDeletableAdapter):
    """
      Manage the mayDelete for Meeting.
      - must have 'Delete objects' on the meeting;
      - if user is Manager, this will remove the meeting including items;
      - if user is MeetingManager, the meeting must be empty to be removed.
    """
    def __init__(self, context):
        self.context = context

    def mayDelete(self, **kwargs):
        '''See docstring in interfaces.py.'''
        if not super(MeetingContentDeletableAdapter, self).mayDelete():
            return False

        if not self.context.getRawItems():
            return True

        member = api.user.get_current()
        if member.has_role('Manager'):
            return True


class OrgContentDeletableAdapter(APContentDeletableAdapter):
    """
      Manage the mayDelete for organization.
      This will remove the 'Remove' button when user is on the 'own_org'.
    """
    def __init__(self, context):
        self.context = context

    def mayDelete(self, **kwargs):
        '''See docstring in interfaces.py.'''
        if not super(OrgContentDeletableAdapter, self).mayDelete():
            return False

        if self.context == get_own_organization():
            return False

        return True


class AdvicePrettyLinkAdapter(PrettyLinkAdapter):
    """ """

    def getLink_cachekey(method, self):
        '''As item title is displayed on advice, invalidate cache if item title changed.'''
        res = super(AdvicePrettyLinkAdapter, self).getLink_cachekey(self)
        item = self.context.aq_inner.aq_parent
        item_title = item.Title()
        return res + (item_title, )

    @ram.cache(getLink_cachekey)
    def getLink(self):
        """Necessary to be able to override the cachekey."""
        return self._getLink()


class ItemPrettyLinkAdapter(PrettyLinkAdapter):
    """Override to take into account PloneMeeting use cases..."""

    def getLink_cachekey(method, self):
        '''cachekey method for self.getLink.'''
        res = super(ItemPrettyLinkAdapter, self).getLink_cachekey(self)
        # manage when displayed in availableItems on the meeting_view
        meeting_modified = None
        if displaying_available_items(self.context):
            meeting = getCurrentMeetingObject(self.context)
            if meeting:
                meeting_modified = meeting.modified()
        # manage takenOverBy
        current_member_id = None
        takenOverBy = self.context.getTakenOverBy()
        if takenOverBy:
            current_member_id = api.user.get_current().getId()
        # manage when displaying the icon with informations about
        # the predecessor living in another MC
        predecessor_modified = None
        predecessor = self._predecessorFromOtherMC()
        if predecessor:
            predecessor_modified = predecessor.modified()
        # manage otherMC to send to, and cloned to
        # indeed we need to know where to send/have been sent if selected/unselected, ...
        ann = IAnnotations(self.context)
        other_mc_to_clone_to = [
            destMeetingConfigId for destMeetingConfigId in self.context.getOtherMeetingConfigsClonableTo()]
        other_mc_cloned_to_ann_keys = [
            destMeetingConfigId for destMeetingConfigId in self.context.listOtherMeetingConfigsClonableTo().keys()
            if self.context._getSentToOtherMCAnnotationKey(destMeetingConfigId) in ann]
        return res + (meeting_modified,
                      takenOverBy,
                      current_member_id,
                      predecessor_modified,
                      other_mc_to_clone_to,
                      other_mc_cloned_to_ann_keys)

    @ram.cache(getLink_cachekey)
    def getLink(self):
        """Necessary to be able to override the cachekey."""
        return self._getLink()

    def _predecessorFromOtherMC(self):
        predecessor = self.context.getPredecessor()
        if predecessor and predecessor.portal_type != self.context.portal_type:
            return predecessor
        return None

    def _leadingIcons(self):
        """
          Manage icons to display before the icons managed by PrettyLink._icons.
        """
        res = []

        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(self.context)
        usedItemAttributes = cfg.getUsedItemAttributes()

        if displaying_available_items(self.context):
            meeting = getCurrentMeetingObject(self.context)
            # there could be no meeting if we opened an item from the available items view
            if meeting:
                # Item is in the list of available items, check if we
                # must show a deadline- or late-related icon.
                if self.context.wfConditions().isLateFor(meeting):
                    # A late item, or worse: a late item not respecting the freeze deadline.
                    if meeting.attributeIsUsed('deadlineFreeze') and \
                       not self.context.lastValidatedBefore(meeting.getDeadlineFreeze()):
                        res.append(('deadlineKo.png', translate('icon_help_publish_freeze_ko',
                                                                domain="PloneMeeting",
                                                                context=self.request)))
                    else:
                        res.append(('late.png', translate('icon_help_late',
                                                          domain="PloneMeeting",
                                                          context=self.request)))
                elif (meeting.queryState() == 'created') and \
                        meeting.attributeIsUsed('deadlinePublish') and \
                        not self.context.lastValidatedBefore(meeting.getDeadlinePublish()):
                    res.append(('deadlineKo.png', translate('icon_help_publish_deadline_ko',
                                                            domain="PloneMeeting",
                                                            context=self.request)))

        itemState = self.context.queryState()
        if itemState == 'delayed':
            res.append(('delayed.png', translate('icon_help_delayed',
                                                 domain="PloneMeeting",
                                                 context=self.request)))
        elif itemState == 'refused':
            res.append(('refused.png', translate('icon_help_refused',
                                                 domain="PloneMeeting",
                                                 context=self.request)))
        elif itemState == 'returned_to_proposing_group':
            res.append(('return_to_proposing_group.png',
                        translate('icon_help_returned_to_proposing_group',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'returned_to_proposing_group_proposed':
            res.append(('goTo_returned_to_proposing_group_proposed.png',
                        translate('icon_help_returned_to_proposing_group_proposed',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'returned_to_proposing_group_prevalidated':
            res.append(('goTo_returned_to_proposing_group_prevalidated.png',
                        translate('icon_help_returned_to_proposing_group_prevalidated',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'prevalidated':
            res.append(('prevalidate.png', translate('icon_help_prevalidated',
                                                     domain="PloneMeeting",
                                                     context=self.request)))
        elif itemState == 'accepted_but_modified':
            res.append(('accepted_but_modified.png', translate('icon_help_accepted_but_modified',
                                                               domain="PloneMeeting",
                                                               context=self.request)))
        elif itemState == 'accepted_out_of_meeting':
            res.append(('accept_out_of_meeting.png',
                        translate('icon_help_accepted_out_of_meeting',
                                  domain="PloneMeeting",
                                  context=self.request,
                                  default=translate('accepted_out_of_meeting',
                                                    domain="plone",
                                                    context=self.request))))
        elif itemState == 'accepted_out_of_meeting_emergency':
            res.append(('accept_out_of_meeting_emergency.png',
                        translate('icon_help_accepted_out_of_meeting_emergency',
                                  domain="PloneMeeting",
                                  context=self.request,
                                  default=translate('accepted_out_of_meeting_emergency',
                                                    domain="plone",
                                                    context=self.request))))
        elif itemState == 'pre_accepted':
            res.append(('pre_accepted.png', translate('icon_help_pre_accepted',
                                                      domain="PloneMeeting",
                                                      context=self.request)))
        elif itemState == 'postponed_next_meeting':
            res.append(('postponed_next_meeting.png',
                        translate('icon_help_postponed_next_meeting',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'marked_not_applicable':
            res.append(('marked_not_applicable.png',
                        translate('icon_help_marked_not_applicable',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'removed':
            res.append(('removed.png',
                        translate('icon_help_removed',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'waiting_advices':
            res.append(('wait_advices_from_proposed.png',
                        translate('icon_help_waiting_advices',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'itemcreated_waiting_advices':
            res.append(('wait_advices_from_itemcreated.png',
                        translate('icon_help_waiting_advices_from_itemcreated',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'proposed_waiting_advices':
            res.append(('wait_advices_from_proposed.png',
                        translate('icon_help_waiting_advices_from_proposed',
                                  domain="PloneMeeting",
                                  context=self.request)))
        elif itemState == 'prevalidated_waiting_advices':
            res.append(('wait_advices_from_prevalidated.png',
                        translate('icon_help_waiting_advices_from_prevalidated',
                                  domain="PloneMeeting",
                                  context=self.request)))

        # Display icons about sent/cloned to other meetingConfigs
        clonedToOtherMCIds = self.context._getOtherMeetingConfigsImAmClonedIn()
        toLocalizedTime = None
        for clonedToOtherMCId in clonedToOtherMCIds:
            # Append a tuple with name of the icon and a list containing
            # the msgid and the mapping as a dict
            # if item sent to the other mc is inserted into a meeting,
            # we display the meeting date
            emergency = clonedToOtherMCId in self.context.getOtherMeetingConfigsClonableToEmergency()
            clonedToOtherMC = getattr(tool, clonedToOtherMCId)
            msgid = emergency and 'sentto_othermeetingconfig_emergency' or 'sentto_othermeetingconfig'
            msg = translate(msgid,
                            mapping={'meetingConfigTitle': safe_unicode(clonedToOtherMC.Title())},
                            domain="PloneMeeting",
                            context=self.request)

            clonedBrain = self.context.getItemClonedToOtherMC(clonedToOtherMCId, theObject=False)
            # do not check on linkedMeetingDate because it may contains '1950/01/01',
            # see linkedMeetingDate indexer in indexes.py
            if clonedBrain.linkedMeetingUID != ITEM_NO_PREFERRED_MEETING_VALUE:
                # avoid instantiating toLocalizedTime more than once
                toLocalizedTime = toLocalizedTime or self.context.restrictedTraverse('@@plone').toLocalizedTime
                long_format = clonedBrain.linkedMeetingDate.hour() and True or False
                msg = msg + u' ({0})'.format(toLocalizedTime(clonedBrain.linkedMeetingDate, long_format=long_format))
            iconName = emergency and "clone_to_other_mc_emergency" or "clone_to_other_mc"
            # manage the otherMeetingConfigsClonableToPrivacy
            if 'privacy' in clonedToOtherMC.getUsedItemAttributes():
                iconName += "_{0}".format(clonedBrain.privacy)
                msg = msg + u' ({0})'.format(translate(clonedBrain.privacy,
                                                       domain="PloneMeeting",
                                                       context=self.request))
            res.append(("{0}.png".format(iconName), msg))

        # if not already cloned to another mc, maybe it will be?
        # we could have an item to clone to 2 other MCs, one already sent, not the other...
        otherMeetingConfigsClonableTo = self.context.getOtherMeetingConfigsClonableTo()
        for otherMeetingConfigClonableToId in otherMeetingConfigsClonableTo:
            # already cloned?
            if otherMeetingConfigClonableToId in clonedToOtherMCIds:
                continue

            # Append a tuple with name of the icon and a list containing
            # the msgid and the mapping as a dict
            otherMeetingConfigClonableTo = getattr(tool, otherMeetingConfigClonableToId)
            emergency = otherMeetingConfigClonableToId in self.context.getOtherMeetingConfigsClonableToEmergency()
            msgid = emergency and 'will_be_sentto_othermeetingconfig_emergency' or \
                'will_be_sentto_othermeetingconfig'
            iconName = emergency and "will_be_cloned_to_other_mc_emergency" or "will_be_cloned_to_other_mc"
            msg = translate(msgid,
                            mapping={'meetingConfigTitle': safe_unicode(
                                     otherMeetingConfigClonableTo.Title())},
                            domain="PloneMeeting",
                            context=self.request)
            # manage the otherMeetingConfigsClonableToPrivacy
            suffix = ''
            if 'otherMeetingConfigsClonableToPrivacy' in usedItemAttributes and \
               'privacy' in otherMeetingConfigClonableTo.getUsedItemAttributes():
                if otherMeetingConfigClonableToId in self.context.getOtherMeetingConfigsClonableToPrivacy():
                    suffix = "_secret"
                else:
                    suffix = "_public"
                msg = msg + u' ({0})'.format(translate(suffix[1:],
                                                       domain="PloneMeeting",
                                                       context=self.request))
            res.append(("{0}{1}.png".format(iconName, suffix),
                        msg))

        # display an icon if item is sent from another mc
        predecessor = self._predecessorFromOtherMC()
        if predecessor:
            predecessorCfg = tool.getMeetingConfig(predecessor)
            predecessorMeeting = predecessor.getMeeting()
            predecessor_state = predecessor.queryState()
            translated_state = translate(predecessor_state, domain='plone', context=self.request)
            if not predecessorMeeting:
                res.append(('cloned_not_decided.png',
                            translate('icon_help_cloned_not_presented',
                                      domain="PloneMeeting",
                                      mapping={'meetingConfigTitle': safe_unicode(predecessorCfg.Title()),
                                               'predecessorState': translated_state},
                                      context=self.request,
                                      default="Sent from ${meetingConfigTitle}, "
                                      "original item is \"${predecessorState}\".")))
            else:
                if predecessor_state in predecessorCfg.getItemPositiveDecidedStates():
                    res.append(('cloned_and_decided.png',
                                translate(
                                    'icon_help_cloned_and_decided',
                                    mapping={'meetingDate': tool.formatMeetingDate(predecessorMeeting),
                                             'meetingConfigTitle': safe_unicode(predecessorCfg.Title()),
                                             'predecessorState': translated_state},
                                    domain="PloneMeeting",
                                    context=self.request,
                                    default="Sent from ${meetingConfigTitle} (${meetingDate}), original item is "
                                    "\"${predecessorState}\".")))
                else:
                    res.append(('cloned_not_decided.png',
                                translate('icon_help_cloned_not_decided',
                                          mapping={'meetingDate': tool.formatMeetingDate(predecessorMeeting),
                                                   'meetingConfigTitle': safe_unicode(predecessorCfg.Title()),
                                                   'predecessorState': translated_state},
                                          domain="PloneMeeting",
                                          context=self.request,
                                          default="Sent from ${meetingConfigTitle} (${meetingDate}), original item is "
                                          "\"${predecessorState}\".")))

        # display icons if element is down the workflow or up for at least second time...
        # display it only for items before state 'validated'
        downOrUpWorkflowAgain = self.context.downOrUpWorkflowAgain()
        if downOrUpWorkflowAgain == "down":
            res.append(('wf_down.png', translate('icon_help_wf_down',
                                                 domain="PloneMeeting",
                                                 context=self.request)))
        elif downOrUpWorkflowAgain == "up":
            res.append(('wf_up.png', translate('icon_help_wf_up',
                                               domain="PloneMeeting",
                                               context=self.request)))

        # In some cases, it does not matter if an item is inMeeting or not.
        if 'oralQuestion' in usedItemAttributes:
            if self.context.getOralQuestion():
                res.append(('oralQuestion.png', translate('this_item_is_an_oral_question',
                                                          domain="PloneMeeting",
                                                          context=self.request)))
        if 'emergency' in usedItemAttributes:
            # display an icon if emergency asked/accepted/refused
            itemEmergency = self.context.getEmergency()
            if itemEmergency == 'emergency_asked':
                res.append(('emergency_asked.png', translate('emergency_asked',
                                                             domain="PloneMeeting",
                                                             context=self.request)))
            elif itemEmergency == 'emergency_accepted':
                res.append(('emergency_accepted.png', translate('emergency_accepted',
                                                                domain="PloneMeeting",
                                                                context=self.request)))
            elif itemEmergency == 'emergency_refused':
                res.append(('emergency_refused.png', translate('emergency_refused',
                                                               domain="PloneMeeting",
                                                               context=self.request)))
        if 'takenOverBy' in usedItemAttributes:
            takenOverBy = self.context.getTakenOverBy()
            if takenOverBy:
                # if taken over, display a different icon if taken over by current user or not
                user = api.user.get_current()
                takenOverByCurrentUser = bool(user.getId() == takenOverBy)
                iconName = takenOverByCurrentUser and 'takenOverByCurrentUser.png' or 'takenOverByOtherUser.png'
                res.append((iconName, translate(u'Taken over by ${fullname}',
                                                domain="PloneMeeting",
                                                mapping={'fullname': safe_unicode(tool.getUserName(takenOverBy))},
                                                context=self.request)))

        if self.context.getIsAcceptableOutOfMeeting():
            res.append(('acceptable_out_of_meeting.png',
                        translate('PloneMeeting_label_isAcceptableOutOfMeeting',
                                  domain="PloneMeeting",
                                  context=self.request)))
        return res


class MeetingPrettyLinkAdapter(PrettyLinkAdapter):
    """
      Override to take into account PloneMeeting use cases...
    """

    def _leadingIcons(self):
        """
          Manage icons to display before the icons managed by PrettyLink._icons.
        """
        res = []
        if self.context.getExtraordinarySession():
            res.append(('extraordinarySession.png',
                        translate('this_meeting_is_extraodrinary_session',
                                  domain="PloneMeeting",
                                  context=self.request)))
        return res


class PMAnnexPrettyLinkAdapter(AnnexPrettyLinkAdapter):
    """
      Override to take into account PloneMeeting use cases...
    """

    def getLink_cachekey(method, self):
        '''cachekey method for self.getLink.'''
        res = super(PMAnnexPrettyLinkAdapter, self).getLink_cachekey(self)
        # check also MeetingConfig modified as updating categorized elements
        # from the ContentCategory will update MeetingConfig.modified
        tool = api.portal.get_tool('portal_plonemeeting')
        # maximize cache on calling getMeetingConfig from parent
        cfg = tool.getMeetingConfig(self.context.aq_parent)
        return res + (cfg.modified(), )

    @ram.cache(getLink_cachekey)
    def getLink(self):
        """Necessary to be able to override the cachekey."""
        return self._getLink()


class PMWfHistoryAdapter(ImioWfHistoryAdapter):
    """
      Override the imio.history ImioHistoryAdapter.
    """

    def __init__(self, context):
        super(PMWfHistoryAdapter, self).__init__(context)
        self.tool = api.portal.get_tool('portal_plonemeeting')
        self.cfg = self.tool.getMeetingConfig(self.context)

    def ignorableHistoryComments(self):
        """Add some more ignorable history comments."""
        ignorable_history_comment = super(PMWfHistoryAdapter, self).ignorableHistoryComments()
        ignorable_history_comment += (u'create_meeting_item_from_template_comments',
                                      u'create_from_predecessor_comments',
                                      u'{0}_comments'.format(DUPLICATE_AND_KEEP_LINK_EVENT_ACTION),
                                      u'{0}_comments'.format(DUPLICATE_EVENT_ACTION),
                                      u'wf_transition_triggered_by_application')
        return ignorable_history_comment

    def mayViewComment(self, event):
        """
          By default, every p_event comment is viewable except for MeetingItem, if
          'hideItemHistoryCommentsToUsersOutsideProposingGroup' is enabled in the MeetingConfig,
          only members of the group manging item at event['review_state'] will be able to access
          history comment.
        """
        userMayAccessComment = True
        if self.context.meta_type == 'MeetingItem':
            if self.cfg.getHideItemHistoryCommentsToUsersOutsideProposingGroup() and \
               not self.tool.isManager(self.context):
                userOrgUids = self.tool.get_orgs_for_user(the_objects=False)
                group_managing_item_uid = \
                    self.context.adapted()._getGroupManagingItem(event['review_state']).UID()
                if group_managing_item_uid not in userOrgUids:
                    userMayAccessComment = False
        return userMayAccessComment

    def get_history_data(self):
        """WF hsitory is mixed with datachanges history."""
        history = super(PMWfHistoryAdapter, self).get_history_data()
        res = []
        for event in history:
            new_event = event.copy()
            if new_event['action'] != '_datachange_':
                res.append(new_event)
        return res


class PMDataChangesHistoryAdapter(ImioWfHistoryAdapter):
    """ """

    history_type = 'data_changes'

    def get_history_data(self):
        """WF history is mixed with datachanges history."""
        history = super(PMDataChangesHistoryAdapter, self).get_history_data()
        full_datachanges_history = []
        # first pass, keep datachanges
        for event in history:
            new_event = event.copy()
            if new_event['action'] == '_datachange_':
                full_datachanges_history.append(new_event)

        # second pass, compute datachanges
        res = []
        i = -1
        full_datachanges_history.reverse()
        while (i + 1) < len(full_datachanges_history):
            i += 1
            new_event = full_datachanges_history[i].copy()
            new_event['changes'] = {}
            new_event['type'] = self.history_type
            for name, oldValue in full_datachanges_history[i]['changes'].iteritems():
                widgetName = self.context.getField(name).widget.getName()
                if widgetName == 'RichWidget':
                    if xhtmlContentIsEmpty(oldValue):
                        val = '-'
                    else:
                        newValue = findNewValue(self.context, name, full_datachanges_history, i - 1)
                        # Compute the diff between oldValue and newValue
                        iMsg, dMsg = getHistoryTexts(self.context, event)
                        comparator = HtmlDiff(oldValue, newValue, iMsg, dMsg)
                        val = comparator.get()
                    new_event['changes'][name] = val
                elif widgetName == 'BooleanWidget':
                    label = oldValue and 'Yes' or 'No'
                    new_event['changes'][name] = translate(label, domain="plone", context=self.request)
                elif widgetName == 'TextAreaWidget':
                    val = oldValue.replace('\r', '').replace('\n', '<br/>')
                    new_event['changes'][name] = val
                elif widgetName == 'SelectionWidget':
                    allValues = self.context.getField(name).Vocabulary(self.context)
                    val = allValues.getValue(oldValue or '')
                    new_event['changes'][name] = val or '-'
                elif widgetName == 'MultiSelectionWidget':
                    allValues = self.context.getField(name).Vocabulary(self.context)
                    val = [allValues.getValue(v) for v in oldValue]
                    if not val:
                        val = '-'
                    else:
                        val = '<br/>'.join(val)
                    new_event['changes'][name] = val
                else:
                    new_event['changes'][name] = oldValue
            res.append(new_event)
        return res


class PMEmergencyChangesHistoryAdapter(BaseImioHistoryAdapter):
    """ """

    history_type = 'emergency_changes'
    history_attr_name = 'emergency_changes_history'


class PMCompletenessChangesHistoryAdapter(BaseImioHistoryAdapter):
    """ """

    history_type = 'completeness_changes'
    history_attr_name = 'completeness_changes_history'


class Criteria(eeaCriteria):
    """
      Override method that gets criteria to be able to manage various use cases :
      - for meetings : get the criteria from the MeetingConfig (searches_items) and filter
        out elements not in MeetingConfig.getDashboardAvailableItemsFilters and not in
        MeetingConfig.getDashboardPresentedItemsFilters;
      - for listing of items : filter out criteria no in MeetingConfig.getDashboardItemsFilters;
      - for listing of meetings : filter out criteria no in MeetingConfig.getDashboardMeetingsFilters.
    """

    def manage_criteria_cachekey(method, self, context):
        '''cachekey method for self.compute_criteria.'''
        return context, str(context.REQUEST._debug)

    def __init__(self, context):
        """ """
        self.context, self.criteria = self.compute_criteria(context)

    @ram.cache(manage_criteria_cachekey)
    def compute_criteria(self, context):
        """ """
        req = context.REQUEST
        # return really stored widgets when necessary
        if 'portal_plonemeeting' in context.absolute_url() or \
           req.get('enablingFacetedDashboard', False) or \
           (req.get('SERVER_URL') == 'http://foo' or
                req.get('PARENTS', [])[0] == api.portal.get_tool('portal_setup')):  # migrating
            super(Criteria, self).__init__(context)
            return self.context, self.criteria
        try:
            tool = api.portal.get_tool('portal_plonemeeting')
        except InvalidParameterError:
            # in case 'portal_plonemeeting' is not available, use original criteria behaviour
            super(Criteria, self).__init__(context)
            return self.context, self.criteria
        cfg = tool.getMeetingConfig(context)
        if not cfg:
            super(Criteria, self).__init__(context)
            return self.context, self.criteria
        # meeting view
        kept_filters = []
        resultsperpagedefault = 20
        meeting_view = False
        if IMeeting.providedBy(context):
            meeting_view = True
            is_displaying_available_items = displaying_available_items(context)
            self.context = cfg.searches.searches_items
            if is_displaying_available_items:
                kept_filters = cfg.getDashboardMeetingAvailableItemsFilters()
                resultsperpagedefault = cfg.getMaxShownAvailableItems()
            else:
                kept_filters = cfg.getDashboardMeetingLinkedItemsFilters()
                resultsperpagedefault = cfg.getMaxShownMeetingItems()
        else:
            # on a faceted?  it is a pmFolder or a subFolder of the pmFolder
            resultsperpagedefault = cfg.getMaxShownListings()
            if IFacetedNavigable.providedBy(context):
                # listings of items has some configuration but not listings of meetings
                if context.getId() == 'searches_items':
                    kept_filters = cfg.getDashboardItemsListingsFilters()
                    self.context = cfg.searches.searches_items
                elif context.getId() == 'searches_meetings':
                    self.context = cfg.searches.searches_meetings
                    self.criteria = self._criteria()
                    return self.context, self.criteria
                elif context.getId() == 'searches_decisions':
                    self.context = cfg.searches.searches_decisions
                    self.criteria = self._criteria()
                    return self.context, self.criteria
                else:
                    self.context = cfg.searches
                    self.criteria = self._criteria()
                    return self.context, self.criteria

        res = PersistentList()
        for criterion in self._criteria():
            if meeting_view and criterion.widget == u'sorting':
                # keep it only of displaying available items, default sorting
                # is set on 'getProposingGroup', if not displaying available items
                # the sorting widget is not kept so sorting is disabled for presented items
                if is_displaying_available_items:
                    new_criterion = Criterion()
                    new_criterion.update(**criterion.__dict__)
                    new_criterion.default = u'getProposingGroup'
                    res.append(new_criterion)
                continue
            if criterion.section != u'advanced' or \
               criterion.__name__ in kept_filters:
                # create new object to avoid modifying stored one
                new_criterion = Criterion()
                new_criterion.update(**criterion.__dict__)
                # manage default value for the 'resultsperpage' criterion
                if criterion.widget == ResultsPerPageWidget.widget_type:
                    new_criterion.default = resultsperpagedefault
                res.append(new_criterion)
        self.criteria = res
        return self.context, self.criteria


class CompoundCriterionBaseAdapter(object):

    def __init__(self, context):
        self.context = context
        self.request = self.context.REQUEST
        self.tool = api.portal.get_tool('portal_plonemeeting')
        self.cfg = self.tool.getMeetingConfig(self.context)

    @property
    def query(self):
        ''' '''
        return {}


# cachekeys useable for CompoundCriterionAdapters
def query_request_cachekey(method, self):
    '''cachekey method for caching for the time of a request.'''
    return str(self.request._debug)


def query_user_groups_cachekey(method, self):
    '''cachekey method for caching as long as global users/groups
       associations did not change.'''
    # always check cfg.modified() as queries are portal_type aware
    cfg_modified = self.cfg and self.cfg.modified() or datetime.now()
    return self.context.modified(), api.user.get_current().getId(), \
        self.tool._users_groups_value(), cfg_modified


def query_meeting_config_modified_cachekey(method, self):
    '''cachekey method for caching as long as MeetingConfig not modified.'''
    cfg_modified = self.cfg and self.cfg.modified() or datetime.now()
    return self.context.modified(), cfg_modified


class LastDecisionsAdapter(CompoundCriterionBaseAdapter):

    @property
    def query_last_decisions(self):
        '''Patch the query 'getDate' to not limit the search
           to 'today' but 60 days in the future.'''
        if not self.cfg:
            return {}
        # remove the 'last-decisions' adapter from query so we may parse it
        # or it will lead to a RuntimeError: maximum recursion depth exceeded
        query = [term for term in self.context.query if term[u'i'] != u'CompoundCriterion']
        parsedQuery = parseFormquery(self.context, query)
        # change the second date of getDate query, aka the 'max' date
        parsedQuery['getDate']['query'][1] = DateTime() + 60
        return parsedQuery

    # we may not ram.cache methods in same file with same name...
    query = query_last_decisions


class ItemsOfMyGroupsAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemsofmygroups(self):
        '''Queries all items of groups of the current user, no matter wich suffix
           of the group the user is in.'''
        if not self.cfg:
            return {}
        userOrgUids = self.tool.get_orgs_for_user(only_selected=False, the_objects=False)
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'getProposingGroup': {'query': userOrgUids}, }

    # we may not ram.cache methods in same file with same name...
    query = query_itemsofmygroups


class MyItemsTakenOverAdapter(CompoundCriterionBaseAdapter):

    def myitemstakenover_cachekey(method, self):
        '''cachekey method for every CompoundCriterion adapters.'''
        return str(self.request._debug)

    @property
    @ram.cache(myitemstakenover_cachekey)
    def query_myitemstakenover(self):
        '''Queries all items that current user take over.'''
        if not self.cfg:
            return {}
        member = api.user.get_current()
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'getTakenOverBy': {'query': member.getId()}, }

    # we may not ram.cache methods in same file with same name...
    query = query_myitemstakenover


class ItemsInCopyAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemsincopy(self):
        '''Queries all items for which the current user is in copyGroups.'''
        if not self.cfg:
            return {}
        userPloneGroups = self.tool.get_plone_groups_for_user()
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'getCopyGroups' use 'OR' by default
                'getCopyGroups': {'query': userPloneGroups}, }

    # we may not ram.cache methods in same file with same name...
    query = query_itemsincopy


class BaseItemsToValidateOfHighestHierarchicLevelAdapter(CompoundCriterionBaseAdapter):

    def _query(self, prefix_review_state=''):
        '''Return a list of items that the user can validate regarding his highest hierarchic level.
           So if a user is 'prereviewer' and 'reviewier', the search will only return items
           in state corresponding to his 'reviewer' role.'''
        if not self.cfg:
            return {}
        userPloneGroupIds = self.tool.get_plone_groups_for_user()
        highestReviewerLevel = self.cfg._highestReviewerLevel(userPloneGroupIds)
        if not highestReviewerLevel:
            # in this case, we do not want to display a result
            # we return an unknown review_state
            return _find_nothing_query(self.cfg.getItemTypeName())
        reviewers = reviewersFor(self.cfg.getItemWorkflow())
        review_states = reviewers[highestReviewerLevel]
        # specific management for workflows using the 'pre_validation' wfAdaptation
        if highestReviewerLevel == 'reviewers' and \
            ('pre_validation' in self.cfg.getWorkflowAdaptations() or
             'pre_validation_keep_reviewer_permissions' in self.cfg.getWorkflowAdaptations()) and \
           review_states == ['proposed']:
            review_states = ['prevalidated']

        reviewProcessInfos = []
        # apply prefix_review_state on review_states
        review_states = [
            '{0}{1}'.format(prefix_review_state, review_state)
            for review_state in review_states]
        for plone_group_id in userPloneGroupIds:
            if plone_group_id.endswith('_%s' % highestReviewerLevel):
                # append group name without suffix
                org_uid = plone_group_id.split('_')[0]
                reviewProcessInfo = [
                    '{0}__reviewprocess__{1}'.format(org_uid, review_state)
                    for review_state in review_states]
                reviewProcessInfos.extend(reviewProcessInfo)
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'reviewProcessInfo': {'query': reviewProcessInfos}, }


class ItemsToValidateOfHighestHierarchicLevelAdapter(
        BaseItemsToValidateOfHighestHierarchicLevelAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstovalidateofhighesthierarchiclevel(self):
        return self._query()

    # we may not ram.cache methods in same file with same name...
    query = query_itemstovalidateofhighesthierarchiclevel


class ItemsToCorrectToValidateOfHighestHierarchicLevelAdapter(
        BaseItemsToValidateOfHighestHierarchicLevelAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstocorrecttovalidateofhighesthierarchiclevel(self):
        return self._query(prefix_review_state='returned_to_proposing_group_')

    # we may not ram.cache methods in same file with same name...
    query = query_itemstocorrecttovalidateofhighesthierarchiclevel


class AllItemsToValidateOfHighestHierarchicLevelAdapter(
        BaseItemsToValidateOfHighestHierarchicLevelAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_allitemstovalidateofhighesthierarchiclevel(self):
        to_validate_query = self._query()
        to_correct_to_validate_query = self._query(prefix_review_state='returned_to_proposing_group_')
        query = merge_queries([to_validate_query, to_correct_to_validate_query])
        return query

    # we may not ram.cache methods in same file with same name...
    query = query_allitemstovalidateofhighesthierarchiclevel


class BaseItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter(CompoundCriterionBaseAdapter):

    def _query(self, prefix_review_state=''):
        '''This will check for user highest reviewer level of each of his groups and return these items and
           items of lower reviewer levels.
           This search works if the workflow manage reviewer levels where higher reviewer level
           can validate lower reviewer levels EVEN IF THE USER IS NOT IN THE CORRESPONDING PLONE SUBGROUP.
           For example with a 3 levels reviewer workflow, called review1 (lowest level),
           review2 and review3 (highest level) :
           - reviewer1 may validate items in reviewer1;
           - reviewer2 may validate items in reviewer1 and reviewer2;
           - reviewer3 may validate items in reviewer1, reviewer2 and reviewer3.
           So get highest hierarchic level of each group of the user and
           take into account lowest levels too.'''
        if not self.cfg:
            return {}
        # search every highest reviewer level for each group of the user
        userOrgUids = self.tool.get_orgs_for_user(the_objects=False)
        userPloneGroups = self.tool.get_plone_groups_for_user()
        reviewProcessInfos = []
        for org_uid in userOrgUids:
            ploneGroups = []
            # find Plone groups of the organization the user is in
            ploneGroups = [userPloneGroupId for userPloneGroupId in userPloneGroups
                           if userPloneGroupId.startswith('%s_' % org_uid)]
            # now that we have Plone groups of the organization
            # we can get highest hierarchic level and find sub levels
            highestReviewerLevel = self.cfg._highestReviewerLevel(ploneGroups)
            if not highestReviewerLevel:
                continue
            foundLevel = False
            reviewers = reviewersFor(self.cfg.getItemWorkflow())
            for reviewer_suffix, review_states in reviewers.items():
                if not foundLevel and not reviewer_suffix == highestReviewerLevel:
                    continue
                foundLevel = True
                # specific management for workflows using the 'pre_validation' or
                # 'pre_validation_keep_reviewer_permissions' wfAdaptation
                if reviewer_suffix == 'reviewers' and \
                    ('pre_validation' in self.cfg.getWorkflowAdaptations() or
                     'pre_validation_keep_reviewer_permissions' in self.cfg.getWorkflowAdaptations()) and \
                   review_states == ['proposed']:
                    review_states = ['prevalidated']
                review_states = [
                    '%s%s' % (prefix_review_state, review_state) for review_state in review_states]
                reviewProcessInfo = [
                    '%s__reviewprocess__%s' % (org_uid, review_state) for review_state in review_states]
                reviewProcessInfos.extend(reviewProcessInfo)
        if not reviewProcessInfos:
            # in this case, we do not want to display a result
            # we return an unknown review_state
            return _find_nothing_query(self.cfg.getItemTypeName())
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'reviewProcessInfo': {'query': reviewProcessInfos}, }


class ItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter(
        BaseItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstovalidateofeveryreviewerlevelsandlowerlevels(self):
        return self._query()

    # we may not ram.cache methods in same file with same name...
    query = query_itemstovalidateofeveryreviewerlevelsandlowerlevels


class ItemsToCorrectToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter(
        BaseItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstocorrecttovalidateofeveryreviewerlevelsandlowerlevels(self):
        return self._query(prefix_review_state='returned_to_proposing_group_')

    # we may not ram.cache methods in same file with same name...
    query = query_itemstocorrecttovalidateofeveryreviewerlevelsandlowerlevels


class AllItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter(
        BaseItemsToValidateOfEveryReviewerLevelsAndLowerLevelsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_allitemstovalidateofeveryreviewerlevelsandlowerlevels(self):
        to_validate_query = self._query()
        to_correct_to_validate_query = self._query(prefix_review_state='returned_to_proposing_group_')
        query = merge_queries([to_validate_query, to_correct_to_validate_query])
        return query

    # we may not ram.cache methods in same file with same name...
    query = query_allitemstovalidateofeveryreviewerlevelsandlowerlevels


class BaseItemsToValidateOfMyReviewerGroupsAdapter(CompoundCriterionBaseAdapter):

    def _query(self, prefix_review_state=''):
        '''Return a list of items that the user could validate.  So it returns every items the current
           user is able to validate at any state of the validation process.  So if a user is 'prereviewer'
           and 'reviewer' for a group, the search will return items in both states.'''
        if not self.cfg:
            return {}
        userPloneGroups = self.tool.get_plone_groups_for_user()
        reviewProcessInfos = []
        reviewers = reviewersFor(self.cfg.getItemWorkflow())
        for userPloneGroupId in userPloneGroups:
            for reviewer_suffix, review_states in reviewers.items():
                # current user may be able to validate at at least
                # one level of the entire validation process, we take it into account
                if userPloneGroupId.endswith('_%s' % reviewer_suffix):
                    # specific management for workflows using the 'pre_validation' wfAdaptation
                    if reviewer_suffix == 'reviewers' and \
                        ('pre_validation' in self.cfg.getWorkflowAdaptations() or
                         'pre_validation_keep_reviewer_permissions' in self.cfg.getWorkflowAdaptations()) and \
                       review_states == ['proposed']:
                        review_states = ['prevalidated']
                    org_uid = userPloneGroupId.split('_')[0]
                    review_states = [
                        '%s%s' % (prefix_review_state, review_state) for review_state in review_states]
                    reviewProcessInfo = [
                        '%s__reviewprocess__%s' % (org_uid, review_state) for review_state in review_states]
                    reviewProcessInfos.extend(reviewProcessInfo)

        if not reviewProcessInfos:
            # in this case, we do not want to display a result
            # we return an unknown review_state
            return _find_nothing_query(self.cfg.getItemTypeName())
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'reviewProcessInfo': {'query': reviewProcessInfos}, }


class ItemsToValidateOfMyReviewerGroupsAdapter(BaseItemsToValidateOfMyReviewerGroupsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstovalidateofmyreviewergroups(self):
        return self._query()

    # we may not ram.cache methods in same file with same name...
    query = query_itemstovalidateofmyreviewergroups


class ItemsToCorrectToValidateOfMyReviewerGroupsAdapter(BaseItemsToValidateOfMyReviewerGroupsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstocorrecttovalidateoffmyreviewergroups(self):
        '''Queries all items that current user may correct and in returned_proposed state.'''
        return self._query(prefix_review_state='returned_to_proposing_group_')

    # we may not ram.cache methods in same file with same name...
    query = query_itemstocorrecttovalidateoffmyreviewergroups


class AllItemsToValidateOfMyReviewerGroupsAdapter(BaseItemsToValidateOfMyReviewerGroupsAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_allitemstovalidateoffmyreviewergroups(self):
        to_validate_query = self._query()
        to_correct_to_validate_query = self._query(prefix_review_state='returned_to_proposing_group_')
        query = merge_queries([to_validate_query, to_correct_to_validate_query])
        return query

    # we may not ram.cache methods in same file with same name...
    query = query_allitemstovalidateoffmyreviewergroups


class BaseItemsToCorrectAdapter(CompoundCriterionBaseAdapter):

    def _query(self, review_states):
        if not self.cfg:
            return {}
        # for every review_states check what roles are able to edit
        # so we will get groups suffixes linked to these roles and find relevant groups
        wfTool = api.portal.get_tool('portal_workflow')
        itemWF = wfTool.getWorkflowsFor(self.cfg.getItemTypeName())[0]
        reviewProcessInfos = []
        for review_state in review_states:
            if review_state in itemWF.states:
                roles = itemWF.states[review_state].permission_roles[ModifyPortalContent]
                suffixes = [suffix for suffix, role in MEETINGROLES.items() if role in roles]
                userOrgUids = self.tool.get_orgs_for_user(suffixes=suffixes, the_objects=False)
                if userOrgUids:
                    for userOrgUid in userOrgUids:
                        reviewProcessInfos.append('%s__reviewprocess__%s' % (userOrgUid, review_state))
        if not reviewProcessInfos:
            return _find_nothing_query(self.cfg.getItemTypeName())
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'reviewProcessInfo': {'query': reviewProcessInfos}, }


class ItemsToCorrectAdapter(BaseItemsToCorrectAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstocorrect(self):
        '''Queries all items that current user may correct.'''
        return self._query(review_states=['returned_to_proposing_group'])

    # we may not ram.cache methods in same file with same name...
    query = query_itemstocorrect


class ItemsToAdviceAdapter(CompoundCriterionBaseAdapter):

    def _query(self, include_hidden_during_redaction=True):
        '''Queries all items for which the current user must give an advice.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # Consider not_given, asked_again and hidden_during_redaction advices,
        # this search will return 'not delay-aware' and 'delay-aware' advices
        indexAdvisers = [org_uid + '_advice_not_given' for org_uid in org_uids] + \
            ['delay__' + org_uid + '_advice_not_given' for org_uid in org_uids] + \
            [org_uid + '_advice_asked_again' for org_uid in org_uids] + \
            ['delay__' + org_uid + '_advice_asked_again' for org_uid in org_uids]
        if include_hidden_during_redaction:
            indexAdvisers += \
                ['{0}_advice_{1}'.format(org_uid, HIDDEN_DURING_REDACTION_ADVICE_VALUE)
                 for org_uid in org_uids] + \
                ['delay__{0}_advice_{1}'.format(org_uid, HIDDEN_DURING_REDACTION_ADVICE_VALUE)
                 for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstoadvice(self):
        return self._query()

    # we may not ram.cache methods in same file with same name...
    query = query_itemstoadvice


class ItemsToAdviceWithoutHiddenDuringRedactionAdapter(ItemsToAdviceAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstoadvicewithouthiddenduringredaction(self):
        return self._query(include_hidden_during_redaction=False)

    # we may not ram.cache methods in same file with same name...
    query = query_itemstoadvicewithouthiddenduringredaction


class ItemsToAdviceWithoutDelayAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstoadvicewithoutdelay(self):
        '''Queries all items for which the current user must give an advice without delay.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # Add a '_advice_not_given' at the end of every group id: we want "not given" advices.
        # this search will only return 'not delay-aware' advices
        indexAdvisers = [org_uid + '_advice_not_given' for org_uid in org_uids] + \
            [org_uid + '_advice_asked_again' for org_uid in org_uids] + \
            ['{0}_advice_{1}'.format(org_uid, HIDDEN_DURING_REDACTION_ADVICE_VALUE) for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    # we may not ram.cache methods in same file with same name...
    query = query_itemstoadvicewithoutdelay


class ItemsToAdviceWithDelayAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstoadvicewithdelay(self):
        '''Queries all items for which the current user must give an advice with delay.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # Add a '_advice_not_given' at the end of every group id: we want "not given" advices.
        # this search will only return 'delay-aware' advices
        indexAdvisers = ['delay__' + org_uid + '_advice_not_given' for org_uid in org_uids] + \
            ['delay__' + org_uid + '_advice_asked_again' for org_uid in org_uids] + \
            ['delay__{0}_advice_{1}'.format(org_uid, HIDDEN_DURING_REDACTION_ADVICE_VALUE)
             for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    # we may not ram.cache methods in same file with same name...
    query = query_itemstoadvicewithdelay


class ItemsToAdviceWithExceededDelayAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_itemstoadvicewithexceededdelay(self):
        '''Queries all items for which the current user must give an advice with exceeded delay.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # Add a '_delay_exceeded' at the end of every group id: we want "not given" advices.
        # this search will only return 'delay-aware' advices for wich delay is exceeded
        indexAdvisers = ['delay__' + org_uid + '_advice_delay_exceeded' for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    # we may not ram.cache methods in same file with same name...
    query = query_itemstoadvicewithexceededdelay


class AdvisedItemsAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_adviseditems(self):
        '''Queries items for which an advice has been given.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # advised items are items that has an advice in a particular review_state
        # just append every available meetingadvice state: we want "given" advices.
        # this search will return every advices
        wfTool = api.portal.get_tool('portal_workflow')
        adviceStates = []
        # manage multiple 'meetingadvice' portal_types
        for portal_type in self.tool.getAdvicePortalTypes():
            adviceWF = wfTool.getWorkflowsFor(portal_type.id)[0]
            adviceStates += adviceWF.states.keys()
        # remove duplicates
        adviceStates = tuple(set(adviceStates))
        indexAdvisers = []
        for adviceState in adviceStates:
            indexAdvisers += [org_uid + '_%s' % adviceState for org_uid in org_uids]
            indexAdvisers += ['delay__' + org_uid + '_%s' % adviceState for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    # we may not ram.cache methods in same file with same name...
    query = query_adviseditems


class AdvisedItemsWithDelayAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_adviseditemswithdelay(self):
        '''Queries items for which an advice has been given with delay.'''
        if not self.cfg:
            return {}
        org_uids = self.tool.get_orgs_for_user(suffixes=['advisers'], the_objects=False)
        # advised items are items that has an advice in a particular review_state
        # just append every available meetingadvice state: we want "given" advices.
        # this search will only return 'delay-aware' advices
        wfTool = api.portal.get_tool('portal_workflow')
        adviceStates = []
        # manage multiple 'meetingadvice' portal_types
        for portal_type in self.tool.getAdvicePortalTypes():
            adviceWF = wfTool.getWorkflowsFor(portal_type.id)[0]
            adviceStates += adviceWF.states.keys()
        # remove duplicates
        adviceStates = tuple(set(adviceStates))
        indexAdvisers = []
        for adviceState in adviceStates:
            indexAdvisers += ['delay__' + org_uid + '_%s' % adviceState for org_uid in org_uids]
        # Create query parameters
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                # KeywordIndex 'indexAdvisers' use 'OR' by default
                'indexAdvisers': {'query': indexAdvisers}, }

    # we may not ram.cache methods in same file with same name...
    query = query_adviseditemswithdelay


class DecidedItemsAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_meeting_config_modified_cachekey)
    def query_decideditems(self):
        '''Queries decided items.'''
        if not self.cfg:
            return {}
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'review_state': {'query': self.cfg.getItemDecidedStates()}, }

    # we may not ram.cache methods in same file with same name...
    query = query_decideditems


class PersonalLabelsAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_personal_labels(self):
        '''Special query that will get personal labels defined in DashboardCollection
           query and turn it into ftw.labels compliant personal labels.'''
        if not self.cfg:
            return {}
        # get personal labels to make current user aware and to negativate
        labels = [value for value in self.context.query if value[u'i'] == u'labels']
        if labels:
            member_id = api.user.get_current().getId()
            labels = labels[0][u'v']
            personal_labels = ['{0}:{1}'.format(member_id, label) for label in labels]
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'labels': {'query': personal_labels}, }

    # we may not ram.cache methods in same file with same name...
    query = query_personal_labels


class NegativePersonalLabelsAdapter(CompoundCriterionBaseAdapter):

    @property
    @ram.cache(query_user_groups_cachekey)
    def query_negative_personal_labels(self):
        '''Special query that will get personal labels defined in DashboardCollection
           query and turn personal labels to negative personal values.'''
        if not self.cfg:
            return {}
        # get personal labels to make current user aware and to negativate
        labels = [value for value in self.context.query if value[u'i'] == u'labels']
        if labels:
            member_id = api.user.get_current().getId()
            # if no selected values, the 'v' key is not there...
            labels = labels[0].get('v', [])
            personal_labels = ['{0}:{1}'.format(member_id, label) for label in labels]
        return {'portal_type': {'query': self.cfg.getItemTypeName()},
                'labels': {'not': personal_labels}, }

    # we may not ram.cache methods in same file with same name...
    query = query_negative_personal_labels


class PMCategorizedObjectInfoAdapter(CategorizedObjectInfoAdapter):
    """ """

    def __init__(self, context):
        super(PMCategorizedObjectInfoAdapter, self).__init__(context)
        self.tool = api.portal.get_tool('portal_plonemeeting')
        self.cfg = self.tool.getMeetingConfig(context)
        self.parent = self.context.aq_inner.aq_parent

    def get_infos(self, category, limited=False):
        """A the 'visible_for_groups' info."""
        if not limited:
            visible_for_groups = self._visible_for_groups()
        infos = super(PMCategorizedObjectInfoAdapter, self).get_infos(
            category, limited=limited)
        if not limited:
            infos['visible_for_groups'] = visible_for_groups
        return infos

    def _apply_visible_groups_security(self, group_ids):
        """Compute 'View' permission if annex is confidential,
           apply local_roles and give 'View' to 'AnnexReader' either,
           remove every local_roles and acquire 'View'."""
        if self.parent.meta_type == 'MeetingItem' or \
           self.parent.portal_type in self.tool.getAdvicePortalTypes(as_ids=True):
            # reinitialize permissions in case no more confidential
            # or confidentiality configuration changed
            self.context.__ac_local_roles_block__ = False
            self.context.manage_permission(View, (), acquire=True)
            self.context.manage_permission(AccessContentsInformation, (), acquire=True)
            grp_reader_localroles = [
                grp_id for grp_id in self.context.__ac_local_roles__
                if READER_USECASES['confidentialannex'] in self.context.__ac_local_roles__[grp_id]]
            self.context.manage_delLocalRoles(grp_reader_localroles)
            if self.context.confidential:
                self.context.manage_permission(
                    View,
                    (READER_USECASES['confidentialannex'], 'Manager', 'MeetingManager'),
                    acquire=False)
                self.context.manage_permission(
                    AccessContentsInformation,
                    (READER_USECASES['confidentialannex'], 'Manager', 'MeetingManager'),
                    acquire=False)
                for grp_id in group_ids:
                    self.context.manage_addLocalRoles(
                        grp_id, (READER_USECASES['confidentialannex'], ))
            # self.context.reindexObjectSecurity()

    def _visible_for_groups(self):
        """ """
        groups = []
        if self.context.confidential:
            groups = self._compute_visible_for_groups()

        # apply security if confidential or going from confidential to not confidential
        # in this case, the 'View' permission was not acquired
        if self.context.confidential or \
           not self.context.acquiredRolesAreUsedBy('View'):
            self._apply_visible_groups_security(groups)
        return groups

    @memoize
    def _compute_visible_for_groups(self):
        """ """
        groups = []
        parent_meta_type = self.parent.meta_type
        if parent_meta_type == 'MeetingItem':
            groups = self._item_visible_for_groups()
        elif parent_meta_type == 'Meeting':
            groups = self._meeting_visible_for_groups()
        else:
            # advice
            groups = self._advice_visible_for_groups()
        return groups

    def _item_visible_for_groups(self):
        """ """
        visible_fors = self.cfg.getItemAnnexConfidentialVisibleFor()
        res = []
        res += self._configgroup_groups(visible_fors)
        res += self._reader_groups(visible_fors)
        res += self._suffix_proposinggroup(visible_fors)
        return res

    def _meeting_visible_for_groups(self):
        """ """
        visible_fors = self.cfg.getMeetingAnnexConfidentialVisibleFor()
        res = []
        res += self._configgroup_groups(visible_fors)
        res += self._suffix_profile_proposinggroup(visible_fors)
        return res

    def _advice_visible_for_groups(self):
        """ """
        visible_fors = self.cfg.getAdviceAnnexConfidentialVisibleFor()
        res = []
        res += self._configgroup_groups(visible_fors)
        res += self._reader_groups(visible_fors)
        res += self._suffix_proposinggroup(visible_fors)
        if 'adviser_group' in visible_fors:
            plone_group_id = get_plone_group_id(self.parent.advice_group, 'advisers')
            res.append(plone_group_id)
        return res

    def _configgroup_groups(self, visible_fors):
        """ """
        res = []
        for visible_for in visible_fors:
            if visible_for.startswith(CONFIGGROUPPREFIX):
                suffix = visible_for.replace(CONFIGGROUPPREFIX, '')
                res.append('{0}_{1}'.format(self.cfg.getId(), suffix))
        return res

    def _suffix_proposinggroup(self, visible_fors):
        """ """
        res = []
        groups_managing_item = self.parent.adapted()._getAllGroupsManagingItem()
        for visible_for in visible_fors:
            if visible_for.startswith(PROPOSINGGROUPPREFIX):
                suffix = visible_for.replace(PROPOSINGGROUPPREFIX, '')
                for group_managing_item in groups_managing_item:
                    plone_group_id = get_plone_group_id(group_managing_item.UID(), suffix)
                    res.append(plone_group_id)
        return res

    def _suffix_profile_proposinggroup(self, visible_fors):
        """ """
        res = []
        for visible_for in visible_fors:
            if visible_for.startswith(SUFFIXPROFILEPREFIX):
                res.append(visible_for)
        return res

    def _reader_groups(self, visible_fors):
        """ """
        res = []
        for visible_for in visible_fors:
            if visible_for == '{0}advices'.format(READERPREFIX):
                for org_uid in self.parent.adviceIndex:
                    plone_group_id = get_plone_group_id(org_uid, 'advisers')
                    res.append(plone_group_id)
            elif visible_for == '{0}copy_groups'.format(READERPREFIX):
                res = res + list(self.parent.getAllCopyGroups(auto_real_plone_group_ids=True))
            elif visible_for == '{0}groupsincharge'.format(READERPREFIX):
                groupsInCharge = self.parent.getGroupsInCharge(theObjects=False, includeAuto=True)
                for groupInCharge in groupsInCharge:
                    plone_group_id = get_plone_group_id(groupInCharge, 'observers')
                    res.append(plone_group_id)
        return res


class PMCategorizedObjectAdapter(CategorizedObjectAdapter):
    """ """

    def __init__(self, context, request, categorized_obj):
        super(PMCategorizedObjectAdapter, self).__init__(context, request, categorized_obj)
        self.tool = api.portal.get_tool('portal_plonemeeting')
        self.cfg = self.tool.getMeetingConfig(self.context)

    def can_view(self):

        # is the context a MeetingItem and privacy viewable?
        if self.context.meta_type == 'MeetingItem' and \
           self.cfg.getRestrictAccessToSecretItems() and \
           not self.context.adapted().isPrivacyViewable():
            return False

        # bypass if not confidential
        infos = self.context.categorized_elements[self.categorized_obj.UID()]
        if not infos['confidential']:
            return True

        # bypass for MeetingManagers
        if self.tool.isManager(self.context):
            return True

        # Meeting
        if self.context.meta_type == 'Meeting':
            # if we have a SUFFIXPROFILEPREFIX prefixed group,
            # check using "userIsAmong", this is only done for Meetings
            if set(self.tool.get_plone_groups_for_user()).intersection(infos['visible_for_groups']):
                return True
            # build suffixes to pass to tool.userIsAmong
            suffixes = []
            for group in infos['visible_for_groups']:
                if group.startswith(SUFFIXPROFILEPREFIX):
                    suffixes.append(group.replace(SUFFIXPROFILEPREFIX, ''))
            if suffixes and self.tool.userIsAmong(suffixes, cfg=self.cfg):
                return True
            return False

        return True


class IconifiedCategoryConfigAdapter(object):
    """ """
    def __init__(self, context):
        """ """
        self.context = context

    @memoize
    def get_config(self):
        """ """
        tool = api.portal.get_tool('portal_plonemeeting')
        # manage the css.py file generation necessary CSS, in this case, context is the portal
        # we return portal as the config root so css file is generated with every existing categories
        # found in every MeetingConfigs
        if self.context.portal_type == 'Plone Site':
            return self.context
        try:
            cfg = tool.getMeetingConfig(self.context)
        except AttributeError:
            cfg = None
        return cfg and cfg.annexes_types or cfg


class IconifiedCategoryGroupAdapter(object):
    """ """
    def __init__(self, config, context):
        """ """
        self.config = config
        self.context = context
        self.request = getattr(self.context, 'REQUEST', {})

    @memoize
    def get_group(self):
        """Return right group, depends on :
           - while adding in an item, annex or decisionAnnex;
           - while adding in a meeting or an advice."""
        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(self.context)
        parent = self.context.getParentNode()
        # adding annex to an item
        if self.context.meta_type == 'MeetingItem' or \
           (self.context.portal_type in ('annex', 'annexDecision') and parent.meta_type == 'MeetingItem'):
            isItemDecisionAnnex = False
            if self.context.meta_type == 'MeetingItem':
                # it is possible to force to use the item_decision_annexes group
                # or when using quickupload, the typeupload contains the type of element to add
                if self.request.get('force_use_item_decision_annexes_group', False) or \
                   self.request.get('typeupload', None) == 'annexDecision':
                    return cfg.annexes_types.item_decision_annexes

                # we are adding a new annex, get annex portal_type from form_instance
                # manage also the InlineValidation view
                if hasattr(self.request.get('PUBLISHED'), 'form_instance'):
                    form_instance = self.request.get('PUBLISHED').form_instance
                elif (hasattr(self.request.get('PUBLISHED'), 'context',) and
                      hasattr(self.request.get('PUBLISHED').context, 'form_instance')):
                    form_instance = self.request.get('PUBLISHED').context.form_instance
                else:
                    # calling with MeetingItem as context, this is the case when checking
                    # if categories exist and if annexes tab should be displayed
                    return cfg.annexes_types.item_annexes

                if getattr(form_instance, 'portal_type', '') == 'annexDecision':
                    isItemDecisionAnnex = True
            else:
                if self.context.portal_type == 'annexDecision':
                    isItemDecisionAnnex = True

            if not isItemDecisionAnnex:
                return cfg.annexes_types.item_annexes
            else:
                return cfg.annexes_types.item_decision_annexes

        # adding annex to an advice
        advicePortalTypeIds = tool.getAdvicePortalTypes(as_ids=True)
        if self.context.portal_type in advicePortalTypeIds \
           or parent.portal_type in advicePortalTypeIds:
            return cfg.annexes_types.advice_annexes

        # adding annex to a meeting
        if self.context.meta_type == 'Meeting' or parent.meta_type == 'Meeting':
            return cfg.annexes_types.meeting_annexes

    def get_every_categories(self, only_enabled=True):
        categories = get_categories(self.context, only_enabled=only_enabled)
        self.request['force_use_item_decision_annexes_group'] = True
        categories = categories + get_categories(self.context, only_enabled=only_enabled)
        self.request['force_use_item_decision_annexes_group'] = False
        return categories


class PMGenerablePODTemplatesAdapter(GenerablePODTemplatesAdapter):
    """ """

    def get_all_pod_templates(self):
        """Query by MeetingConfig."""
        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(self.context)
        if not cfg:
            return []
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog.unrestrictedSearchResults(
            object_provides={'query': IPODTemplate.__identifier__,
                             'not': IDashboardPODTemplate.__identifier__},
            # PloneMeeting, just added following line
            path={'query': '/'.join(cfg.getPhysicalPath())},
            sort_on='getObjPositionInParent'
        )
        pod_templates = [self.context.unrestrictedTraverse(brain.getPath()) for brain in brains]

        return pod_templates


class PMDashboardGenerablePODTemplatesAdapter(DashboardGenerablePODTemplatesAdapter):
    """ """

    def get_all_pod_templates(self):
        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(self.context)
        query = {'object_provides': {'query': IDashboardPODTemplate.__identifier__},
                 'sort_on': 'getObjPositionInParent'}
        # filter on MeetingConfig if we are in it
        if cfg:
            query['path'] = {'query': '/'.join(cfg.getPhysicalPath())}
        else:
            # out of a MeetingConfig
            query['getConfigId'] = EMPTY_STRING

        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog.unrestrictedSearchResults(**query)
        pod_templates = [self.context.unrestrictedTraverse(brain.getPath()) for brain in brains]

        return pod_templates

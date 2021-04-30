from pyflarum.client.classes.FlarumSession import FlarumSession
from pyflarum.client.classes.FlarumMyUser import FlarumMyUser

from pyflarum.client.classes.flarum.FlarumForum import FlarumForum

from pyflarum.client.classes.flarum.FlarumUser import FlarumUser
from pyflarum.client.classes.flarum.FlarumUsers import FlarumUsers
from pyflarum.client.classes.flarum.FlarumGroups import FlarumGroup, FlarumGroups

from pyflarum.client.classes.flarum.FlarumDiscussions import FlarumDiscussion, FlarumDiscussions
from pyflarum.client.classes.flarum.FlarumPosts import FlarumPost

from pyflarum.client.classes.extensions.Flarum_Tags import FlarumPostDiscussionTagsData, FlarumTagUserMixin
from pyflarum.client.classes.extensions.FriendsOfFlarum_Polls import FoF_Poll, FoF_PollOption


if __name__ == "__main__":
    print(
        FoF_Poll,
        FoF_PollOption,
        FlarumPostDiscussionTagsData,
        FlarumTagUserMixin,
        FlarumPost,
        FlarumDiscussion,
        FlarumDiscussions,
        FlarumGroup,
        FlarumGroups,
        FlarumUser,
        FlarumUsers,
        FlarumForum,
        FlarumMyUser,
        FlarumSession
    )

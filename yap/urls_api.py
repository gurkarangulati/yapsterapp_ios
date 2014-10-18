from django.conf.urls import patterns, include, url
from yap.views_api import *

urlpatterns = patterns('yap.views_api',
	url(r'^create/$',CreateYap.as_view()),
	url(r'^delete/$',DeleteYap.as_view()),
	url(r'^follow/request/$',FollowRequest.as_view()),
	url(r'^follow/accept/$',FollowAccept.as_view()),
	url(r'^follow/deny/$',FollowDeny.as_view()),
	url(r'^follow/unfollow/$',FollowUnfollow.as_view()),
	url(r'^follow/unrequest/$',FollowUnrequest.as_view()),
	url(r'^like/$',LikeObj.as_view()),
	url(r'^unlike/$',UnlikeObj.as_view()),
	url(r'^reyap/$',ReyapObj.as_view()),
	url(r'^unreyap/$',UnreyapObj.as_view()),
	url(r'^reyap/delete/$',DeleteReyap.as_view()),
	url(r'^listen/$',ListenToAnObj.as_view()),
	url(r'^listen/time_listened/$',ListenTimeListened.as_view()),
	url(r'^listen/hashtag_clicked/$',ListenHashtagClicked.as_view()),
	url(r'^listen/user_handle_clicked/$',ListenUserHandleClicked.as_view()),
	url(r'^listen/user_yapped_clicked/$',ListenUserYappedClicked.as_view()),
	url(r'^listen/user_reyapped_clicked/$',ListenUserReyappedClicked.as_view()),
	url(r'^listen/picture_clicked/$',ListenPictureClicked.as_view()),
	url(r'^listen/skip_clicked/$',ListenSkipClicked.as_view()),
	url(r'^explore/channels/load/$',LoadExploreChannels.as_view()),
	url(r'^channels/load/$',LoadYapChannels.as_view()),
	url(r'^following_and_followers/$',ListOfFollowingAndFollowers.as_view()),
	url(r'^push_notification_object_call/$',PushNotificationObjectCall.as_view()),
	url(r'^share/facebook/$',ShareToFacebook.as_view()),
	url(r'^share/twitter/$',ShareToTwitter.as_view()),
	# url(r'^list_of_users_who_liked_object/$', ListOfUsersWhoLikedObject.as_view()),
	# url(r'^list_of_users_who_reyapped_object/$', ListOfUsersWhoReyappedObject.as_view()),
)

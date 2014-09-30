from django.conf.urls import patterns, include, url
from users.views_api import *

urlpatterns = patterns('users.views_api',
	url(r'^profile/info/$',ProfileInfo.as_view()),
	url(r'^profile/stream/$',ProfileStreams.as_view()),
	url(r'^profile/followers/$',ListOfFollowers.as_view()),
	url(r'^profile/following/$',ListOfFollowing.as_view()),
	#url(r'^delete/$',UserDelete.as_view()),
	url(r'^sign_in/$',SignIn.as_view()),
	url(r'^automatic_sign_in/$',AutomaticSignIn.as_view()),
	url(r'^sign_out/$',SignOut.as_view()),
	url(r'^recommended/$',Recommendations.as_view()),
	url(r'^sign_up/verify_email/$',SignUpVerifyEmail.as_view()),
	url(r'^sign_up/verify_username/$',SignUpVerifyUsername.as_view()),
	url(r'^sign_up/$',SignUp.as_view()),
	url(r'^settings/load/$',LoadSettings.as_view()),
	url(r'^profile/load/$',LoadProfile.as_view()),
	url(r'^profile/edit_profile_picture/$',EditProfilePicture.as_view()),
	url(r'^profile/edit/$',EditProfile.as_view()),
	url(r'^settings/edit/$',EditSettings.as_view()),
	url(r'^setsession/$','session_id'),
	url(r'^forgot_password/request_for_email/$',ForgotPasswordRequestForEmail.as_view()),
	url(r'^forgot_password/reset_password_request/$',ResetPasswordRequest.as_view()),
)
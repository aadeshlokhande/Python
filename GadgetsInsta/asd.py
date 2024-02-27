import instaloader

bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, '_datboii.aadii')


print("biography = ",profile.biography)
print("biography_hashtags = ",profile.biography_hashtags)
print("biography_mentions = ",profile.biography_mentions)
print("blocked_by_viewer = ",profile.blocked_by_viewer)
print("business_category_name = ",profile.business_category_name)
print("external_url = ",profile.external_url)
print("followed_by_viewer = ",profile.followed_by_viewer)
print("followees = ",profile.followees)
print("followers = ",profile.followers)
print("follows_viewer = ",profile.follows_viewer)
print("full_name = ",profile.full_name)
print("has_blocked_viewer = ",profile.has_blocked_viewer)
print("has_highlight_reels = ",profile.has_highlight_reels)
print("has_public_story = ",profile.has_public_story)
print("has_requested_viewer = ",profile.has_requested_viewer)
print("has_viewable_story = ",profile.has_viewable_story)
print("igtvcount = ",profile.igtvcount)
print("is_business_account = ",profile.is_business_account)
print("is_private = ",profile.is_private)
print("is_verified = ",profile.is_verified)
print("mediacount = ",profile.mediacount)
print("profile_pic_url = ",profile.profile_pic_url)
print("profile_pic_url_no_iphone = ",profile.profile_pic_url_no_iphone)
print("requested_by_viewer = ",profile.requested_by_viewer)
print("userid = ",profile.userid)
print("username = ",profile.username)
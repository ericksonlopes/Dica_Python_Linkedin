import instaloader

insta = instaloader.Instaloader()
user = 'erickson.lds'

insta.download_profile(user, profile_pic_only=True)

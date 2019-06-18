from datetime import datetime
from telegram import Bot
import instaloader

bot = Bot(token="1386687051:644a6ee0274561139103ef8843cde64a5499fb51",
          base_url="https://tapi.bale.ai/",
          base_file_url="https://tapi.bale.ai/file/")


PUBLIC_PROFILE = "balemessenger"


L = instaloader.Instaloader(download_geotags=True,
                                 download_comments=True,
                                 save_metadata=True, bot=bot)


instaloadercontext_query_timestamps = dict()  # type: Dict[str, List[float]]
L.context._graphql_query_timestamps = instaloadercontext_query_timestamps.copy()
filter = lambda post: post.date > datetime(2019, 4, 12)
profiles = {L.check_profile_id(PUBLIC_PROFILE)}
L.download_profiles(profiles, profile_pic=False, fast_update=True, raise_errors=True)
L.download_profiles(profiles, profile_pic=False, fast_update=True, raise_errors=True)


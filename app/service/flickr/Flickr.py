import app.service.flickr.flickr_config as config
import flickr_api

flickr_api.set_keys(config.API_KEY, config.API_SECRET)


class FlickrService:
    def get_public_feed(self, tags):
        print('Search Flickr for %s' % tags)
        photo_items = flickr_api.Walker(flickr_api.Photo.search, tags=tags)
        print("Got %d result(s) for %s" % (len(photo_items), tags))
        return photo_items

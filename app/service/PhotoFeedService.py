import generated.photofeed_pb2 as photo_feed
import generated.photofeed_pb2_grpc as photo_feed_grpc

from app.service.flickr.Flickr import FlickrService


class PhotoFeedService(photo_feed_grpc.PhotoServiceServicer):
    def GetPublicPhotos(self, request: photo_feed.PhotoSearchRequest, context):
        photo_items = FlickrService.get_public_feed(FlickrService(), request.tags)
        max_result = 10
        photos = []
        for item in photo_items:
            photo = photo_feed.Photo(
                title=item.title,
                description=item.description,
                author=item.owner.username,
                url=item.url_m
            )
            photos.append(photo)

            if len(photos) == max_result:
                break

        photo_result = photo_feed.PhotoResult(
            title=request.tags,
            photos=photos
        )
        print('Returning %d result(s)' % len(photos))
        return photo_result

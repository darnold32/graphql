import typing
import strawberry

@strawberry.type
class Designer:
    name: str

@strawberry.type
class Studio:
    name: str

@strawberry.type
class VideoGame:
    studio: 'Studio'
    designer: 'Designer'
    name: str


videoGames = [
    VideoGame(
        studio=Studio(
            name='ICLA'
        ),
        designer=Designer(
            name='Dan Arnold'
        ),
        name='Pokemon Brilliant Diamond'
    ),
    VideoGame(
        studio=Studio(
            name='MDHR'
        ),
        designer=Designer(
            name='Dan Arnold'
        ),
        name='Cuphead'
    )
]


def get_video_games():
    return videoGames



@strawberry.type
class Query:
    videoGames: typing.List[VideoGame] = strawberry.field(resolver=get_video_games)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_videoGame(self, studioName: str, designerName: str, videoGameName:str) -> typing.List[VideoGame]:
        videoGames.append(VideoGame(
        studio=Studio(
            name=studioName
        ),
        designer=Designer(
            name=designerName
        ),
        name=videoGameName
    ))
        return videoGames

schema = strawberry.Schema(query=Query, mutation=Mutation)
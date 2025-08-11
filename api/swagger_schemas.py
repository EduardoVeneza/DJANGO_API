from drf_yasg import openapi

trail_post_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, readOnly=True, title="ID"),
        'title': openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Title",
            maxLength=255,
            minLength=1,
            default="My Trail"
        ),
        'description': openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Description",
            minLength=1,
            default="My trail description"
        ),
        'create_at': openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATE,
            readOnly=True,
            title="Create at"
        ),
        'number_of_steps': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            title="Number of steps",
            minimum=0,
            maximum=9223372036854776000,
            default=10
        ),
        'autor': openapi.Schema(
            type=openapi.TYPE_STRING,
            title="autor",
            minLength=1,
            default=""
        ),
    },
    required=['title', 'description']
)


trail_put_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, readOnly=True, title="ID"),
        'title': openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Title",
            maxLength=255,
            minLength=1,
            default="My Trail Title Updated"
        ),
        'description': openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Description",
            minLength=1,
            default="My trail description Updated"
        ),
        'create_at': openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATE,
            readOnly=True,
            title="Create at"
        ),
        'number_of_steps': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            title="Number of steps",
            minimum=0,
            maximum=9223372036854776000,
            default=10
        ),
    },
    required=['title', 'description']
)

StepCreateSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["title", "description", "position"],
    properties={
        "title": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Title",
            maxLength=255,
            minLength=1,
            default="My Step Title"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Description",
            minLength=1,
            default="My Step Description"
        ),
        "position": openapi.Schema(
            type=openapi.TYPE_INTEGER,
            title="Position",
            minimum=0,
            default=1
        ),
        "video_url": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="video_url",
            minLength=1,
            default="http://example.com/video.mp4",
        )
    }
)
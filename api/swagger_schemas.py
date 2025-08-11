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

AttachmentSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=[],
    properties={
        "name": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Name",
            minLength=0,
            default="Attachment Name",
            nullable=True,
        ),
        "phone": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Phone",
            minLength=0,
            default="+55 71 99999-9999",
            nullable=True,
        ),
        "email": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_EMAIL,
            title="Email",
            default="usuario@email.com",
            nullable=True,
        ),
        "video_duration": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Video Duration (timedelta format)",
            default="00:05:30",
            description="Formato hh:mm:ss",
            nullable=True,
        ),
        "file_url": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_URI,
            title="File URL",
            default="http://example.com/file.pdf",
            nullable=True,
        ),
    }
)

LinkSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["link"],
    properties={
        "link": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_URI,
            title="Link URL",
            minLength=1,
            default="http://example.com/resource"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING,
            title="Description",
            minLength=0,
            default="Descrição opcional do link",
            nullable=True,
        ),
    },
    read_only=['step']
)

watched_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'watched': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status de visualização')
            },
            required=['watched']
            )
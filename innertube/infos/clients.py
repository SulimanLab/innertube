from . import models
from . import services
from . import devices

Web = models.ClientInfo \
(
    name    = 'WEB',
    version = '2.20210223.09.00',
    device  = devices.Web,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)

WebMusic = models.ClientInfo \
(
    name    = 'WEB_REMIX',
    version = '0.1',
    device  = devices.Web,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30'),
)

WebKids = models.ClientInfo \
(
    name    = 'WEB_KIDS',
    version = '2.1.3',
    device  = devices.Web,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU'),
)

WebStudio = models.ClientInfo \
(
    name    = 'WEB_CREATOR',
    version = '1.20210223.01.00',
    device  = devices.Web,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'),
)

Android = models.ClientInfo \
(
    name    = 'ANDROID',
    version = '16.07.34',
    device  = devices.Android,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w'),
)

AndroidMusic = models.ClientInfo \
(
    name    = 'ANDROID_MUSIC',
    version = '4.16.51',
    device  = devices.Android,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI'),
)

AndroidKids = models.ClientInfo \
(
    name    = 'ANDROID_KIDS',
    version = '6.02.3',
    device  = devices.Android,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk'),
)

AndroidStudio = models.ClientInfo \
(
    name    = 'ANDROID_CREATOR',
    version = '21.06.103',
    device  = devices.Android,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8'),
)

Ios = models.ClientInfo \
(
    name    = 'IOS',
    version = '16.05.7',
    device  = devices.Ios,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc'),
)

IosMusic = models.ClientInfo \
(
    name    = 'IOS_MUSIC',
    version = '4.16.1',
    device  = devices.Ios,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s'),
)

IosKids = models.ClientInfo \
(
    name    = 'IOS_KIDS',
    version = '5.42.2',
    device  = devices.Ios,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc'),
)

IosStudio = models.ClientInfo \
(
    name    = 'IOS_CREATOR',
    version = '20.47.100',
    device  = devices.Ios,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs'),
)

Tv = models.ClientInfo \
(
    name    = 'TVHTML5',
    version = '7.20210224.00.00',
    device  = devices.Tv,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8'),
)

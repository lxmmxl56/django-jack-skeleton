from logging import getLogger
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

log = getLogger(settings.DEBUG_LOGGER)


def index(request):
    now = timezone.now()
    # log.debug(now)

    # Add a bootstrap color tag and message to this list to display an alert
    alerts = []

    error_alert  = {
        'tag': 'danger',
        'message': _('ERROR: This is just a test.')
    }
    info_alert = {
        'tag': 'info',
        'message': _('Hiya Buddy 🌭')
    }
    alerts.append(info_alert)
    alerts.append(error_alert)

    # Add a title, image src, classes, time, and body text to this list to display a toast
    toasts = []

    error_toast = {
        'classes': 'bg-danger text-white border-0',
        'image_src': 'data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7',
        'title': _('Danger'),
        'time': now - timedelta(minutes=8),
        'body': _("You've successfully read this message.")
    }

    info_toast = {
        'classes': 'bg-info text-white border-0',
        'image_src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAAB3RJTUUH5QMMBikzeDBntgAABINJREFUSMellFtsFGUYhp9/Zme3220p2+2WHiiFCDYRS6FVIwUFEiMmxsSoMUbjFRfEmGhIvOMCEyTxkBguDIkGLvQCL5DoDRcQEakxJpCopIJCsQ2BHmh3u509zczOf/CiB7acwS+Zq3/m+d95v/f7BA9R4amdAAgBAtGBYJ2osS4MfnB+5FJdnE3G8LOGN08cJ/J/4CCeCpXeXyhW1rvnS5cm6uM/VSrm618sztlz7z/wBfMlEKtDpQ9kcn5f5kyBBDM9K3tVT/lM/Mm84ZWoYCo8tRPrYdRblkgobfa6Zb9PlqaJS5em9WWWP+1RG9MbhGLNisfryJcr2A8KNwaE4J1COdxVUdNW+6oxmtZ5xFKKwkgMi5Td+3Jzes0TS4aNZlQ8CBzAEqLfr8gj4xNem85O0dGbZfxcDfq6Q20qTao7ie0IpDS/ZfP+q/e0aBHcEi2h0vtmikFbOFag1ikRhoI/BmopyzRN3UksR2AMSK27K1L33HeTLUvUKGX2lANva6JhlPTGAnZUkfkzxtr2BCueXYpwBJg5YVLboVQ1d7ygWrltCVtrs6vkyx04k0SjMwyejRP+GyXh1bLyhUaiCQszBzcGyr4sSmXGrPuCG/NuKVC7s5myE7WLFK86XDmeYPRqnFR/inizswAH8CsSL5AXgaHI3eCWJWq0MbtKvtztlgoJpzxDNOITaocVUYu2LUtJPxJfBNfGkC9VkMocsy2Ri9wRLkSL1mZP0ZM7SoHrpFtHcdoCZCiYuBwl3ddA0/q6W/6+UA4pB3JYCI7C3CRXg40B2xL9Uul9bincmpsqs2z5JDoruXyigcC1iHcmaXmmAWHfaCqAF0hmCgHacBDDkBBg3WRJwrJ4z6vII5m8tzWfdbELU9TWF7lwJs743zHq2xvp3JzEii6GV6Qmmw+Q2pwWcFDMTVgEFrbiaqXM3pIfvpZz/UhdQ4Z0Vw4LhTdl4w3HaN3cQHt/wy1wqTRZ16cSqgkBe4Cp+bNI1VY8MFMM+nJjAVbOJbkly6W/okyeS5DyYqzpTc16fpMtShsyro8XSA/4EDg9f9b11rdEBKIjVHp/dsbvy46U0NcLdPa6KE/gnkwQIU7rc0mWro7PNakKrmbhZV9K4DPgUDV81iLBukKx0pMbzNPUlqFxYxkbGPmxjmSqjuXbGomnF+d83pYq+OfAx4CshgNElOCf6bPFESuXX9u8vUzufIzJM7XULkvS8WISp2pC5ysIFVnXx68oD/gU+ATwbje0kW8+GhlrN2J8RZdZW7rmcO1kHY1djbRsalhYXNURLnohuUKAVHpizvNDt1O+kMwdnTFvBvPD0LDj/np4Cbq1fgG+KIahIuN6ZFwPqfQA8Abw5Tz8ThU5fCXAWHxVDMWgCcRjG3qXvG45YpsxYLShIjUlL6Tkh0hlhoGDc89CFG+n/EZMAWEIEQw0P1ozULcs8vu0G+yXSneHUtuh0kWtzUUDxwQcBYaqAXeDAwiA75/fzku7V/HFd4O8/3Yvgxeutzq21SMENQgxJmahuZs/vhcc4D+B7F5V5HvLOwAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMS0wMy0xMlQwNjo0MTozMSswMDowMG/ioY0AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjEtMDMtMTJUMDY6NDE6MzErMDA6MDAevxkxAAAAAElFTkSuQmCC',
        'title': _('Hiya'),
        'time': now - timedelta(minutes=4),
        'body': _('Buddy')
    }
    toasts.append(info_toast)
    toasts.append(error_toast)

    return render(request, 'index.html', {
            'alerts': alerts,
            'toasts': toasts,
            'now': now,
        }
    )


@login_required
def restricted_media(request, filename=None, download=False):
    try:
        import os
        from mimetypes import MimeTypes
        content_type, _ = MimeTypes().guess_type(
            os.path.basename(filename)
        )
        if not content_type:
            log.debug(
                "No content-type found for file: %s"
                % os.path.basename(filename)
            )
            content_type = "text/plain"

        url = str(filename)
        try:
            file_name = ReportFile.objects.get(file=url).name
        except ReportFile.DoesNotExist:
            file_name = ReportFile.objects.get(file=os.path.join(settings.MEDIA_ROOT, url)).name
        import urllib
        quoted_filename = urllib.parse.quote(str(filename))
        with open(os.path.join(settings.MEDIA_ROOT, quoted_filename), "rb") as f:
            data = f.read()
            data_start = 0
            data_length = len(data)
            data_end = data_length - 1
            file_length = data_length
            if 'range' in request.headers:
                range = request.headers['range']
                # expecting bytes=0-1
                if 'bytes' in range:
                    if '=' in range:
                        range = range.split('=')[1]
                    elif ' ' in range:
                        range = range.split(' ')[1]
                    if '-' in range:
                        range_start, range_end = range.split('-')
                        if not range_end:
                            range_end = data_end
                        f.seek(int(range_start))
                        # add 1 to the following to be inclusive
                        read_range = int(range_end) - int(range_start) + 1
                        if 1 > read_range:
                            read_range = 1
                        data = f.read(read_range)
                        data_length = len(data)
                        data_start = range_start
                        data_end = range_end
                resp = HttpResponse(data, content_type=content_type, status=206)
                resp['Accept-Ranges'] = 'bytes'
                resp['Content-Length'] = data_length
                resp['Content-Range'] = 'bytes %s-%s/%s' % (data_start, data_end, file_length)
            else:
                resp = HttpResponse(data, content_type=content_type)
            if download:
                resp['Content-Disposition'] = f'attachment; filename="{file_name}"'
            # resp['access-control-allow-origin'] = '*'
            resp['X-Robots-Tag'] = 'noindex, nofollow'
            return resp
    except IOError as ex:
        data = {"file ERROR": str(ex),}
        return JsonResponse(data)

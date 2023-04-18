import datetime
import json
from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response

from .models import CatDirection, CatCoach, CatSession, Session
from .serializers import CatDirectionSerializer, CatCoachSerializer, CatSessionSerializer, SessionSerializer, \
    SessionDetailSerializer


# direction CATEGORY
class CatDirectionAPIList(generics.ListCreateAPIView):
    queryset = CatDirection.objects.all()
    serializer_class = CatDirectionSerializer


class CatDirectionAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatDirection.objects.all()
    serializer_class = CatDirectionSerializer


# coach CATEGORY
class CatCoachDirectionAPIList(generics.ListCreateAPIView):
    queryset = CatCoach.objects.all()
    serializer_class = CatCoachSerializer


class CatCoachDirectionAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatCoach.objects.all()
    serializer_class = CatCoachSerializer


# session CATEGORY
class CatSessionAPIList(generics.ListCreateAPIView):
    queryset = CatSession.objects.all()
    serializer_class = CatSessionSerializer


class CatSessionAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatSession.objects.all()
    serializer_class = CatSessionSerializer


# session
class SessionAPIList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionDetailSerializer


def get_matrix_list(session_list):
    sorted_by_data = sorted(
        session_list,
        key=lambda x: x.get("date_start"), reverse=False
    )

    dates = set(list(map(lambda x: x.get("date_start").strftime("%m/%d/%Y"), sorted_by_data)))
    dates_sorted = sorted(
        list(dates),
        key=lambda x: datetime.strptime(x, "%m/%d/%Y"), reverse=False
    )

    matrix_by_date = []
    for date_str in dates_sorted:
        date = datetime.strptime(date_str, "%m/%d/%Y")
        matrix_list = []
        for session in sorted_by_data:
            session_day = session.get("date_start")
            if date.day == session_day.day and date.month == session_day.month and date.year == session_day.year:
                matrix_list.append(session)

        if matrix_list:
            matrix_by_date.append(matrix_list)

    return matrix_by_date


def get_filtered_list(session_list, query):
    result_list = session_list
    filter_dict = {
        "session": CatSession.objects.all().values(),
        "direction": CatDirection.objects.all().values(),
        "coach": CatCoach.objects.all().values(),
    }
    filter_ids = {
        "session": [],
        "direction": [],
        "coach": [],
    }

    for item in query:
        ids = json.loads(query[item])
        result_list = list(filter(lambda x: x.get(item) in ids, result_list))

    for item in result_list:
        filter_ids["session"].append(item["session_id"])
        filter_ids["direction"].append(item["direction_id"])
        filter_ids["coach"].append(item["coach_id"])

    filter_ids_set = {
        "session": set(filter_ids["session"]),
        "direction": set(filter_ids["direction"]),
        "coach": set(filter_ids["coach"]),
    }

    for item in filter_dict:
        def filter_mapping(x):

            if x.get("id") in filter_ids_set[item]:
                res = {**x, "is_active": True}
            else:
                res = {**x, "is_active": False}

            q = query.get(f'{item}_id')
            q_res = json.loads(q) if q else None

            if not q_res is None and x.get("id") in q_res:
                res = {**res, "is_selected": True}
            else:
                res = {**res, "is_selected": False}

            return res

        filter_dict[item] = list(map(filter_mapping, filter_dict[item]))

    return {
        "list": list(result_list),
        "filter_dict": filter_dict
    }


class SessionsForBoardAPIList(generics.ListAPIView):
    def get(self, request):
        if not request.query_params:
            return Response({
                "filter": {
                    "session": CatSession.objects.all().values(),
                    "direction": CatDirection.objects.all().values(),
                    "coach": CatCoach.objects.all().values(),
                },
                "page_list": get_matrix_list(Session.objects.all().values())
            })

        filtered_result = get_filtered_list(Session.objects.all().values(), request.query_params)

        return Response({
            "filter": filtered_result.get("filter_dict"),
            "page_list": get_matrix_list(filtered_result.get("list"))
        })

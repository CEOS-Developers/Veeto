from django.db import models
from accounts.models import SimpleUser


# 액티비티 (방탈출, 볼링, 보드게임)
class Activity(models.Model):
    name = models.CharField(max_length=20, verbose_name="액티비티 종류")

    def __str__(self):
        return self.name


class Room(models.Model):
    room_name = models.CharField(max_length=100, default="액티비티 같이 해요~!")  # 방 이름(소개) - 50자 이내
    #master = models.ManyToManyField(SimpleUser, through='Own', related_name="rooms_I_own")
    members = models.ManyToManyField(SimpleUser, through='Join', through_fields=('room','user'))  # simpleuser.room_set 또는 rooms.members
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    date = models.DateField()  # 활동 날짜
    time = models.TimeField()  # 활동 시간
    total_number_of_members = models.IntegerField()  # 방 총 인원
    sex_ratio = models.IntegerField(default=0)  # 성비 맞출지 여부 (0-무관, 1-성비맞춤, 2-같은성별만)
    is_Confirm = models.BooleanField(default=False)  # 방 확정여부

    def __str__(self):  # 액티비티+활동날짜시간+총인원 표시
        return self.activity.__str__()+"/ "+str(self.date)+" "+str(self.time)+"("+str(self.total_number_of_members)+")"


class Join(models.Model):
    user = models.ForeignKey(SimpleUser, on_delete=models.PROTECT)
    user_nickname = models.CharField(max_length=15)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_master = models.BooleanField(default=False)

    def __str__(self):  # 방 멤버+방 표시
        if self.is_master == True:
            return self.user.__str__()+"(m) in "+self.room.__str__()
        else:
            return self.user.__str__()+" in "+self.room.__str__()

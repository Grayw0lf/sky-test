from django.db import models
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):
    fio = models.CharField(max_length=255, verbose_name=_('ФИО'))
    date_of_birth = models.DateField(verbose_name=_('Дата рождения'))
    sex = models.IntegerField(verbose_name=_('Пол'))

    class Meta:
        verbose_name = _('Пациент')
        verbose_name_plural = _('Пациенты')

    def __str__(self):
        return self.fio


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, related_name='patients', on_delete=models.CASCADE,
                                verbose_name=_('Пациент'))
    start_date = models.DateField(verbose_name=_('Дата начала'))
    end_date = models.DateField(blank=True, null=True, verbose_name=_('Дата окончания'))
    result = models.IntegerField(null=True, verbose_name=_('Исход лечения'))

    class Meta:
        verbose_name = _('Случай лечения')
        verbose_name_plural = _('Случаи лечения')

    def __str__(self):
        return f"{self.patient.fio} период {self.start_date} - {self.end_date}"


class MedicalDoc(models.Model):
    patient = models.ForeignKey(Patient, related_name='medicaldocs', on_delete=models.CASCADE,
                                verbose_name=_('Пациент'))
    treatment = models.ForeignKey(Treatment, related_name='medicaldocs', on_delete=models.CASCADE,
                                  verbose_name=_('Случай лечения'))
    title = models.CharField(max_length=255, verbose_name=_('Заголовок документа'))
    date_doc = models.DateField(verbose_name=_('Дата документа'))

    class Meta:
        verbose_name = _('Медицинский документ')
        verbose_name_plural =_('Медицинские документы')

    def __str__(self):
        return f"{self.title} - {self.date_doc}"


class BodyDoc(models.Model):
    medicaldoc = models.OneToOneField(MedicalDoc, related_name='bodydoc', on_delete=models.CASCADE,
                                      verbose_name=_('Медицинский документ'))
    content = models.JSONField(verbose_name=_('Наполнение документа'))

    class Meta:
        verbose_name = _('Тело документа')
        verbose_name_plural = _('Тело документа')

    def __str__(self):
        return self.medicaldoc.title

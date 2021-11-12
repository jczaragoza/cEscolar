from django.db import models


class Calificaciones(models.Model):
   calificacion = models.FloatField(blank=True, null=True, verbose_name='Calificación')

   def __str__(self):
        return self.calificacion

   class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
        ordering = ['id']


class Categorias(models.Model):
    nom_categoria = models.CharField(max_length=150, unique=True, verbose_name='Categoría')
    descripcion = models.TextField(max_length=50, blank=True, null=True, verbose_name='Descripción')

    def __str__(self):
        return self.nom_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Corporaciones(models.Model):
    nom_corporacion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Corporación')

    def __str__(self):
        return self.nom_corporacion

    class Meta:
        verbose_name = 'Corporación'
        verbose_name_plural = 'Corporaciones'
        ordering = ['id']


class Cursos(models.Model):
    nom_curso = models.CharField(max_length=255, blank=True, null=True, verbose_name='Curso')
    #categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    horas = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nom_curso

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Colonia(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Personas(models.Model):
    persona = models.CharField(max_length=255, blank=True, null=True)
    curp = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=255, blank=True, null=True)
    #status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.persona

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']


class ProfesorCursos(models.Model):
    profesor_curso = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.profesor_curso

    class Meta:
        verbose_name = 'Prof Cur'
        verbose_name_plural = 'Prof Curs'
        ordering = ['id']


class Profesores(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    a_paterno = models.CharField(max_length=255, blank=True, null=True)
    a_materno = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['id']


class Supervisores(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    a_paterno = models.CharField(max_length=255, blank=True, null=True)
    a_materno = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisores'
        ordering = ['id']
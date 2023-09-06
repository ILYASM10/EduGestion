from django.db import models
from django.contrib.auth.models import User

# Table pour stocker les informations sur les écoles.
class School(models.Model):
    name = models.CharField(max_length=255)  # Nom de l'école.
    address = models.TextField()  # Adresse de l'école. 
# Table pour stocker les rôles des utilisateurs (directeurs, professeurs, etc.).
class Role(models.Model):
    name = models.CharField(max_length=100)  # Nom du rôle.
    # Vous pouvez ajouter d'autres attributs pour gérer les autorisations spécifiques aux rôles.

# Table pour stocker les postes au sein de l'école (directeur, secrétaire, etc.).
class Position(models.Model):
    name = models.CharField(max_length=100)  # Nom du poste.
    roles = models.ManyToManyField(Role)  # Rôles associés au poste.

# Table pour stocker les informations de base sur les utilisateurs.
class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien vers l'utilisateur Django.
    position = models.ForeignKey(Position, on_delete=models.CASCADE)  # Poste de l'utilisateur.
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # École à laquelle l'utilisateur est associé.

# Table pour stocker les informations spécifiques aux professeurs.
class Teacher(UserInformation):
    taught_subjects = models.ManyToManyField('Subject')  # Matières enseignées par le professeur.

# Table pour stocker les informations spécifiques aux directeurs.
class Director(UserInformation):
    pass  # Les directeurs n'ont pas d'attributs spécifiques supplémentaires pour le moment.

# Table pour stocker les informations spécifiques aux secrétaires.
class Secretary(UserInformation):
    pass  # Les secrétaires n'ont pas d'attributs spécifiques supplémentaires pour le moment.

# Table pour stocker les informations spécifiques aux gardiens.
class Janitor(UserInformation):
    pass  # Les gardiens n'ont pas d'attributs spécifiques supplémentaires pour le moment.

# Table pour stocker les informations sur les élèves.
class Student(models.Model):
    last_name = models.CharField(max_length=100)  # Nom de l'élève.
    first_name = models.CharField(max_length=100)  # Prénom de l'élève.
    date_of_birth = models.DateField()  # Date de naissance de l'élève.
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # École à laquelle l'élève est inscrit.
    class_assigned = models.ForeignKey('Class', on_delete=models.CASCADE)  # Classe à laquelle l'élève est assigné.

# Table pour stocker les informations sur les matières enseignées.
class Subject(models.Model):
    name = models.CharField(max_length=100)  # Nom de la matière.

# Table pour stocker les informations sur les années scolaires.
class SchoolYear(models.Model):
    start_date = models.DateField()  # Date de début de l'année scolaire.
    end_date = models.DateField()  # Date de fin de l'année scolaire.

# Table pour stocker les informations sur les trimestres.
class Trimester(models.Model):
    name = models.CharField(max_length=100)  # Nom du trimestre.
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)  # Année scolaire associée.

# Table pour stocker les informations sur les semestres.
class Semester(models.Model):
    name = models.CharField(max_length=100)  # Nom du semestre.
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)  # Année scolaire associée.

# Table pour stocker les informations sur les classes.
class Class(models.Model):
    name = models.CharField(max_length=100)  # Nom de la classe (par ex. "Classe A").
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Professeur principal de la classe.

# Table pour stocker les informations sur les cours.
class Course(models.Model):
    name = models.CharField(max_length=100)  # Nom du cours (par ex. "Mathématiques").
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Professeur responsable du cours.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Matière enseignée dans le cours.
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)  # Classe à laquelle le cours est assigné.

# Table pour stocker les informations sur les notes des élèves.
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Élève associé à la note.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Cours associé à la note.
    trimester = models.ForeignKey(Trimester, on_delete=models.CASCADE)  # Trimestre associé à la note.
    grade = models.DecimalField(max_digits=5, decimal_places=2)  # Note (par ex. 15.5).

# Table pour stocker les informations sur les absences des élèves.
class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Élève associé à l'absence.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Cours associé à l'absence.
    date = models.DateField()  # Date de l'absence.

# Table pour stocker les informations sur l'emploi du temps.
class Schedule(models.Model):
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)  # Classe associée à l'emploi du temps.
    day_of_week = models.CharField(max_length=20)  # Jour de la semaine (par ex. "Lundi").
    start_time = models.TimeField()  # Heure de début.
    end_time = models.TimeField()  # Heure de fin.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Cours programmé dans l'emploi du temps.

# Table pour stocker les informations sur les paiements de scolarité.
class TuitionPayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Élève associé au paiement.
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Montant payé.
    payment_date = models.DateField()  # Date du paiement.

# Table pour stocker les informations sur les moyennes trimestrielles.
class QuarterlyAverage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Élève associé à la moyenne.
    trimester = models.ForeignKey(Trimester, on_delete=models.CASCADE)  # Trimestre associé à la moyenne.
    average = models.DecimalField(max_digits=5, decimal_places=2)  # Moyenne (par ex. 14.8).

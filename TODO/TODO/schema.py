import graphene
from graphene_django import DjangoObjectType
from users.models import TodoUser
from TodoLists.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = TodoUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TodoType)
    # Нахождение всех карточек с заданиями конкретного проекта по его названию
    todo_by_project_name = graphene.List(TodoType,
                                         name=graphene.String(required=False))

    def resolve_all_users(root, info):
        return TodoUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_todo_by_project_name(self, info, name=None):
        todo = ToDo.objects.all()
        if name:
            todo = todo.filter(project__project_name=name)
        return todo


class TodoMutation(graphene.Mutation):
    class Params:
        id = graphene.ID(required=True)
        project = graphene.ID
        text = graphene.String()
        creator = graphene.ID()
        create_date = graphene.DateTime(required=False)
        active = graphene.Boolean()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, id, text, active):
        todo = ToDo.objects.get(pk=id)
        todo.text = text
        todo.active = active
        todo.save()
        return TodoMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


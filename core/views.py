from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Account, Category, Transaction
from .serializers import AccountSerializer, CategorySerializer, TransactionSerializer


# 🔐 Descripción común para todos los endpoints protegidos
auth_note = (
    "🔐 Este endpoint requiere autenticación JWT.\n"
    "Agrega el token de acceso en la cabecera:\n\n"
    "`Authorization: Bearer <tu_token>`"
)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description=f"📄 Listar cuentas del usuario.\n\n{auth_note}"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"➕ Crear una nueva cuenta para el usuario.\n\n{auth_note}"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"✏️ Recuperar los datos de una cuenta específica.\n\n{auth_note}"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"📝 Actualizar parcialmente una cuenta.\n\n{auth_note}"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"❌ Eliminar una cuenta existente.\n\n{auth_note}"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description=f"📄 Listar categorías.\n\n{auth_note}")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"➕ Crear una nueva categoría.\n\n{auth_note}"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"✏️ Recuperar una categoría.\n\n{auth_note}"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"📝 Editar parcialmente una categoría.\n\n{auth_note}"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"❌ Eliminar una categoría.\n\n{auth_note}"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description=f"📄 Listar transacciones del usuario.\n\n{auth_note}"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"➕ Registrar una nueva transacción (gasto o abono).\n\n{auth_note}"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"✏️ Ver detalle de una transacción específica.\n\n{auth_note}"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"📝 Editar parcialmente una transacción.\n\n{auth_note}"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=f"❌ Eliminar una transacción.\n\n{auth_note}"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

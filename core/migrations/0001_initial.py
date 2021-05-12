# Generated by Django 3.1.2 on 2021-05-12 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_rut', models.IntegerField(primary_key=True, serialize=False)),
                ('cli_pnombre', models.CharField(max_length=30)),
                ('cli_apellidopat', models.CharField(max_length=50)),
                ('cli_apellidomat', models.CharField(max_length=50)),
                ('cli_email', models.EmailField(max_length=50)),
                ('cli_telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_rut', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_pnombre', models.CharField(max_length=50)),
                ('emp_apellidopat', models.CharField(max_length=50)),
                ('emp_apellidomat', models.CharField(max_length=50)),
                ('emp_sueldo', models.BigIntegerField()),
                ('emp_telefono', models.IntegerField()),
                ('emp_email', models.EmailField(max_length=30)),
                ('user_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_nombre', models.CharField(max_length=100)),
                ('prod_stock', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prov_nombre', models.CharField(max_length=100)),
                ('prov_rut_empresa', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_descripcion', models.CharField(max_length=45)),
                ('serv_costo', models.BigIntegerField()),
                ('serv_titulo', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_tipo_empleado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_medio_pago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nombre', models.CharField(max_length=20)),
                ('user_contrasena', models.CharField(max_length=20)),
                ('user_desc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_hora_reservada', models.DateField(choices=[['08:00', '08:00'], ['09:00', '09:00'], ['10:00', '10:00'], ['11:00', '11:00'], ['12:00', '12:00'], ['13:00', '13:00'], ['14:00', '14:00'], ['15:00', '15:00'], ['16:00', '16:00'], ['17:00', '17:00'], ['18:00', '18:00'], ['19:00', '19:00'], ['20:00', '20:00']], max_length=5)),
                ('res_fecha_pedido_reserva', models.DateField()),
                ('res_desc_reserva', models.CharField(max_length=200)),
                ('cli_rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='RecepcionPedidoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_cantidad', models.BigIntegerField()),
                ('fecha_recepcion', models.DateField()),
                ('costo_recepcion', models.BigIntegerField(blank=True, null=True)),
                ('prod_nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='RecepcionPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField()),
                ('desc_recepcion', models.CharField(max_length=150)),
                ('emp_rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='desc_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipomarca'),
        ),
        migrations.AddField(
            model_name='producto',
            name='prov_nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.proveedor'),
        ),
        migrations.CreateModel(
            name='PedidoOrdenProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_cantidad', models.BigIntegerField()),
                ('costo_pedido', models.BigIntegerField()),
                ('prod_nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ped_desc_emision', models.CharField(max_length=100)),
                ('ped_fecha_emision', models.DateField()),
                ('emp_rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='PagoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_serv', models.CharField(max_length=50)),
                ('desc_medio_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipopago')),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_utilizada_prod', models.BigIntegerField()),
                ('res_id_reserva', models.BigIntegerField()),
                ('emp_rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empleado')),
                ('prod_nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.producto')),
                ('serv_titulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='desc_tipo_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoempleado'),
        ),
        migrations.CreateModel(
            name='DetalleServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_serv_realizado', models.DateField()),
                ('hora_servicio_realizado', models.CharField(choices=[['08:00', '08:00'], ['09:00', '09:00'], ['10:00', '10:00'], ['11:00', '11:00'], ['12:00', '12:00'], ['13:00', '13:00'], ['14:00', '14:00'], ['15:00', '15:00'], ['16:00', '16:00'], ['17:00', '17:00'], ['18:00', '18:00'], ['19:00', '19:00'], ['20:00', '20:00']], max_length=5)),
                ('servicios_realizados', models.CharField(max_length=150)),
                ('costo_total_servicios', models.BigIntegerField()),
                ('cli_rut', models.IntegerField()),
                ('desc_medio_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.pagoservicio')),
                ('serv_titulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_comuna', models.CharField(max_length=50)),
                ('desc_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='desc_comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.comuna'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='desc_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.region'),
        ),
        migrations.CreateModel(
            name='BoletaFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bol_fac_total', models.BigIntegerField()),
                ('bol_fac_fecha_emision', models.DateField()),
                ('desc_bol_fac', models.CharField(choices=[['Boleta', 'Boleta'], ['Factura', 'Factura']], max_length=7)),
                ('serv_titulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicio')),
            ],
        ),
    ]

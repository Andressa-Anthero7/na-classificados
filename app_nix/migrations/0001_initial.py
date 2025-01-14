# Generated by Django 4.1.10 on 2024-07-31 23:29

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_anunciante', models.CharField(default='Tipo Anunciante', max_length=20)),
                ('nome_razaosocial', models.CharField(max_length=256)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=256)),
                ('img_perfil', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[150, 150], upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='AnuncioVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_veiculo', models.CharField(default='Tipo Veículo', max_length=100)),
                ('nome_marca', models.CharField(max_length=100)),
                ('nome_modelo', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=4)),
                ('combustivel', models.CharField(blank=True, max_length=10, null=True)),
                ('cambio', models.CharField(blank=True, max_length=10, null=True)),
                ('cor', models.CharField(blank=True, max_length=20, null=True)),
                ('portas', models.CharField(blank=True, max_length=10, null=True)),
                ('ipva', models.CharField(blank=True, max_length=10, null=True)),
                ('placa', models.CharField(blank=True, max_length=10, null=True)),
                ('valor', models.CharField(max_length=10)),
                ('acendedor_cigarros', models.CharField(blank=True, max_length=50, null=True)),
                ('air_bags', models.CharField(blank=True, max_length=10, null=True)),
                ('alarme', models.CharField(blank=True, max_length=10, null=True)),
                ('ar_condicionado', models.CharField(blank=True, max_length=20, null=True)),
                ('ar_condicionado_digital', models.CharField(blank=True, max_length=30, null=True)),
                ('ar_condicionado_dual_zone', models.CharField(blank=True, max_length=30, null=True)),
                ('ar_quente', models.CharField(blank=True, max_length=30, null=True)),
                ('assistente_saida_aclive', models.CharField(blank=True, max_length=30, null=True)),
                ('sistema_audio', models.CharField(blank=True, max_length=30, null=True)),
                ('banco_apoio_braco', models.CharField(blank=True, max_length=30, null=True)),
                ('banco_regulagem_eletrica', models.CharField(blank=True, max_length=30, null=True)),
                ('blindado', models.CharField(blank=True, max_length=30, null=True)),
                ('bluetooth', models.CharField(blank=True, max_length=30, null=True)),
                ('calotas', models.CharField(blank=True, max_length=30, null=True)),
                ('camera_re', models.CharField(blank=True, max_length=30, null=True)),
                ('carregador_dispositivo_wireless', models.CharField(blank=True, max_length=50, null=True)),
                ('cd_mp3', models.CharField(blank=True, max_length=30, null=True)),
                ('chaves_keyless', models.CharField(blank=True, max_length=30, null=True)),
                ('chaves_sensor_presenca', models.CharField(blank=True, max_length=30, null=True)),
                ('computador_bordo', models.CharField(blank=True, max_length=30, null=True)),
                ('controle_som_volante', models.CharField(blank=True, max_length=30, null=True)),
                ('controle_eletronico_descida', models.CharField(blank=True, max_length=20, null=True)),
                ('desembacador_traseiro', models.CharField(blank=True, max_length=30, null=True)),
                ('direcao_eletrica', models.CharField(blank=True, max_length=30, null=True)),
                ('direcao_hidraulica', models.CharField(blank=True, max_length=30, null=True)),
                ('encosto_cabeca_traseiro', models.CharField(blank=True, max_length=30, null=True)),
                ('estribo', models.CharField(blank=True, max_length=30, null=True)),
                ('farois_automatico', models.CharField(blank=True, max_length=30, null=True)),
                ('farois_milhas', models.CharField(blank=True, max_length=30, null=True)),
                ('farois_neblina', models.CharField(blank=True, max_length=30, null=True)),
                ('freio_abs', models.CharField(blank=True, max_length=30, null=True)),
                ('gps', models.CharField(blank=True, max_length=30, null=True)),
                ('insulfilm', models.CharField(blank=True, max_length=30, null=True)),
                ('lona_maritima', models.CharField(blank=True, max_length=30, null=True)),
                ('multimidia', models.CharField(blank=True, max_length=30, null=True)),
                ('painel_lcd', models.CharField(blank=True, max_length=30, null=True)),
                ('painel_digital', models.CharField(blank=True, max_length=30, null=True)),
                ('parachoque_cor_veiculo', models.CharField(blank=True, max_length=30, null=True)),
                ('park_assist', models.CharField(blank=True, max_length=30, null=True)),
                ('partida_start_stop', models.CharField(blank=True, max_length=30, null=True)),
                ('piloto_automatico', models.CharField(blank=True, max_length=30, null=True)),
                ('pintura_metalica', models.CharField(blank=True, max_length=30, null=True)),
                ('porta_copo', models.CharField(blank=True, max_length=30, null=True)),
                ('protecao_cacamba', models.CharField(blank=True, max_length=30, null=True)),
                ('radio', models.CharField(blank=True, max_length=30, null=True)),
                ('rebatimento_retrovisores_externos', models.CharField(blank=True, max_length=30, null=True)),
                ('retrovisor_fotocromatico', models.CharField(blank=True, max_length=30, null=True)),
                ('retrovisor_interno_eletrocromico', models.CharField(blank=True, max_length=30, null=True)),
                ('retrovisor_eletrico', models.CharField(blank=True, max_length=30, null=True)),
                ('roda_liga_leve', models.CharField(blank=True, max_length=30, null=True)),
                ('sensor_chuva', models.CharField(blank=True, max_length=30, null=True)),
                ('sensor_estacionamento_dianteiro', models.CharField(blank=True, max_length=30, null=True)),
                ('sensor_estacionamento_traseiro', models.CharField(blank=True, max_length=30, null=True)),
                ('teto_solar', models.CharField(blank=True, max_length=30, null=True)),
                ('teto_panoramico', models.CharField(blank=True, max_length=30, null=True)),
                ('tracao', models.CharField(blank=True, max_length=30, null=True)),
                ('trava_eletrica', models.CharField(blank=True, max_length=30, null=True)),
                ('usb', models.CharField(blank=True, max_length=30, null=True)),
                ('vidro_eletrico', models.CharField(blank=True, max_length=30, null=True)),
                ('vidro_verdes', models.CharField(blank=True, max_length=30, null=True)),
                ('volante_regulagem_altura', models.CharField(blank=True, max_length=30, null=True)),
                ('info_complementares', models.TextField(blank=True, max_length=255, null=True)),
                ('anunciado_por', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('imagem_1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_5', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_6', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_7', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_8', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_9', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
                ('imagem_10', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_leads', models.CharField(max_length=30)),
                ('whatsapp', models.CharField(max_length=13)),
                ('status_aberto', models.CharField(max_length=20)),
                ('status_leads', models.CharField(max_length=8)),
                ('data_recebimento', models.CharField(max_length=50)),
                ('ultimo_user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TagGoogle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('tag_google', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TagGoogleBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('tag_google_body', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tagmeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('tag_meta', models.TextField(max_length=256)),
            ],
        ),
    ]

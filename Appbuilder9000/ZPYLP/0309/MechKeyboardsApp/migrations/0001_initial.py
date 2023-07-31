# Generated by Django 2.2.5 on 2020-12-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyboardList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank='False', default='', max_length=80)),
                ('case', models.CharField(blank='False', choices=[('Project Keyboard Kepler', 'Project Keyboard Kepler'), ('Percent Studio Canoe', 'Percent Studio Canoe'), ('Norbauer Novatouch', 'Norbauer Novatouch'), ('Rama M60-A', 'Rama M60-A'), ('Noxary XRF', 'Noxary XRF'), ('Rama M60-A SEQ2', 'Rama M60-A SEQ2'), ('Crykyn Dawn 75%', 'Crykyn Dawn 75%'), ('Norbauer Norbaforce Mark II', 'Norbauer Norbaforce Mark II'), ('Keycult No.1 TKL Rev.1', 'Keycult No.1 TKL Rev. 1'), ('Project Keyboard Sirius', 'Project Keyboard Sirius'), ('Noxary 268', 'Noxary 268'), ('Rama Kara', 'Rama Kara'), ('Proto[Typist] J-02', 'Proto[Typist] J-02'), ('Funderburker TMOv1', 'Funderburker TMOv1'), ('Zambumon Verne', 'Zambumon Verne'), ('Quantic Kyuu 65%', 'Quantic Kyuu 65%'), ('Mekanisk Tind', 'Mekanisk Tind'), ('Xeno', 'Xeno'), ('Keycult No.2 TKL', 'Keycult No.2 TKL'), ('Project Keyboard Kepler FC65', 'Project Keyboard Kepler FC65'), ('Norbauer Heavy-6', 'Norbauer Heavy-6'), ('Keycult No.1/65', 'Keycult No.1/65'), ('LZ PhysiX', 'LZ PhysiX'), ('Exclusive E8.5 TKL', 'Exclusive E8.5 TKL'), ('Norbauer Heavy-9', 'Norbauer Heavy-9'), ('TGR Jane', 'TGR Jane'), ('The Key Company CandyBar Premium', 'The Key Company CandyBar Premium'), ('Keycult No.1 TKL', 'Keycult No.1 TKL'), ('Smith + Rune Iron 165', 'Smith + Rune Iron 165'), ('Wilba.Tech Thermal', 'Wilba.Tech Thermal'), ('Norbauer Norbaforce', 'Norbauer Norbaforce'), ('Satisfaction 75 r2', 'Satisfaction 75 r2'), ('TGR Jane v2 CE', 'TGR Jane v2 CE'), ('Keycult No.2/65', 'Keycult No.2/65'), ('Rama Koyu', 'Rama Koyu'), ('Demo & Airpotter Arc80 TKL', 'Demo & Airpotter Arc80 TKL'), ('Funderburker TMOv2', 'Funderburker TMOv2'), ('Other', 'Other'), ('Ai03 Keyboards Polaris', 'Ai03 Keyboards Polaris'), ('Exclusive E7-v2', 'Exclusive E7-v2'), ('Think 6.5 v1', 'Think 6.5 v1'), ('Proto[Typist] J-01', 'Proto[Typist] J-01'), ('Dixie Mech Bauer 2', 'Dixie Mech Bauer 2'), ('CannonKeys Brutal 60', 'CannonKeys Brutal 60'), ('Smith + Rune Iron 180', 'Smith + Rune Iron 180'), ('Fox Lab Time TKL', 'Fox Lab Time TKL'), ('Norbauer Heavy Grail', 'Norbauer Grail'), ('Mekanisk Fjell', 'Mekanisk Fjell'), ('Mekanisk Klippe', 'Mekanisk Klippe'), ('TGR Alice', 'TGR Alice'), ('Zambumon Sar', 'Zambumon Sar'), ('OLKB Planck', 'OLKB Planck'), ('Keycult No.2 TKL Rev. 1', 'Keycult No.2 TKL Rev. 1'), ('Percent Studio Canoe Gen2', 'Percent Studio Canoe Gen2'), ('Salamander TKL', 'Salamander TKL'), ('CannonKeys Savage 65', 'CannonKeys Savage 65'), ('Keycult No.1/60', 'Keycult No.1/60'), ('Exclusive E7', 'Exclusive E7'), ('OLKB Preonic', 'OLKB Preonic'), ('Rama M65-B', 'Rama M65-B'), ('TGR 910', 'TGR 910'), ('Think 6.5 v2', 'Think 6.5 v2'), ('Noxary 268.2', 'Noxary 268.2'), ('Exclusive E6.5', 'Exclusive E6.5'), ('Dixie Mech Bauer', 'Dixie Mech Bauer'), ('CannonKeys Chimera 65', 'CannonKeys Chimera 65'), ('Satisfaction 75', 'Satisfaction 75'), ('Project Keyboard Tengu', 'Project Keyboard Tengu'), ('Rama M65-A', 'Rama M65-A'), ('Prime Keyboards Prime_E', 'Prime Keyboards Prime_E'), ('Reconsiderit Southpaw 65+', 'Reconsiderit Southpaw 65+'), ('TGR Jane v2', 'TGR Jane v2'), ('Rama U80-A SEQ2', 'Rama U80-ASEQ2'), ('Lin Montage', 'Lin Montage')], default='', max_length=80)),
                ('pcb', models.CharField(blank='False', choices=[('Hotswap', 'Hotswap'), ('No PCB(handwired)', 'No PCB(handwired)'), ('Solderable', 'Solderable')], default='', max_length=30)),
                ('plate', models.CharField(blank='False', choices=[('POM Half Plate', 'POM Half Plate'), ('Stainless Steel Half Plate', 'Stainless Steel Half Plate'), ('Integrated Half Plate', 'Integrated Half Plate'), ('Carbon Fiber Half Plate', 'Carbon Fiber Half Plate'), ('Aluminum Half Plate', 'Aluminum Half Plate'), ('POM', 'POM'), ('Carbon Fiber', 'Carbon Fiber'), ('Acrylic Half Plate', 'Acrylic Half Plate'), ('Polycarbonate', 'Polycarbonate'), ('Acrylic', 'Acrylic'), ('Titanium Half Plate', 'Titanium Half Plate'), ('Other', 'Other'), ('None', 'None'), ('Aluminum', 'Aluminum'), ('Brass', 'Brass'), ('Stainless Steel', 'Stainless Steel'), ('Polycarbonate Half Plate', 'Polycarbonate Half Plate'), ('Integrated', 'Integrated'), ('Brass Half Plate', 'Brass Half Plate'), ('Titanium', 'Titanium')], default='', max_length=50)),
                ('stabilizers', models.CharField(blank='False', choices=[('EverGlide Stabilizers', 'EverGlide Stabilizers'), ('None', 'None'), ('Others', 'Others'), ('Durock Stabilizers', 'Durock Stabilizers'), ('Cherry Stabilizers', 'Cherry Stabilizers'), ('Zeal PC Stabilizers', 'Zeal PC Stabilizers'), ('C3 Equalz Stabilizers', 'C3 Equalz Stabilizers')], max_length=30)),
                ('switches', models.CharField(blank='False', choices=[('Cherry MX Blue', 'Cherry MX Blue'), ('Kailh Pro Heavy Sage', 'Kailh Pro Heavy Sage'), ('Cherry MX Silent Red', 'Cherry MX Silent Red'), ('Cherry MX Yellow', 'Cherry MX Yellow'), ('Gateron Silent Yellow', 'Gateron Silent Yellow'), ('Gateron Inks', 'Gateron Inks'), ('Kailh Pro Purple', 'Kailh Pro Purple'), ('Gateron Silent Red', 'Gateron Silent Red'), ('Kailh Pro Light Green', 'Kailh Pro Light Green'), ('Gateron Silent Brown', 'Gateron Silent Brown'), ('Gateron Blue', 'Gateron Blue'), ('Zeal Tealio', 'Zeal Tealio'), ('Cherry MX Black', 'Cherry MX Black'), ('Cherry MX White', 'Cherry MX White'), ('Gateron Yellow', 'Gateron Yellow'), ('Cherry MX Red', 'Cherry MX Red'), ('Kailh Brown', 'Kailh Brown'), ('Kailh Pro Burgundy', 'Kailh Pro Burgundy'), ('Cherry MX Clear', 'Cherry MX Clear'), ('C3 Tangerines', 'C3 Tangerines'), ('Kailh Box Navy', 'Kailh Box Navy'), ('Kailh Pro Heavy Plum', 'Kailh Pro Heavy Plum'), ('Kailh Red', 'Kailh Red'), ('Gateron Brown', 'Gateron Brown'), ('Cherry MX Silent Black', 'Cherry MX Silent Black'), ('Kailh Blue', 'Kailh Blue'), ('Gateron Silent Inks', 'Gateron Silent Inks'), ('Cherry MX Speed Silvers', 'Cherry MX Speed Silvers'), ('Gateron Clear', 'Gateron Clear'), ('Kailh Pro Heavy Berry', 'Kailh Pro Heavy Berry'), ('Zeal Healio', 'Zeal Healio'), ('Cherry MX Grey', 'Cherry MX Grey'), ('Kailh Black', 'Kailh Black'), ('Zeal Zealio', 'Zeal Zealio'), ('Gateron Silent Clear', 'Gateron Silent Clear'), ('Gateron Silent Black', 'Gateron Silent Black'), ('Others', 'Others'), ('Zeal Sakurio', 'Zeal Sakurio'), ('Gateron Red', 'Gateron Red'), ('Gateron Black', 'Gateron Black'), ('Cherry MX Brown', 'Cherry MX Brown'), ('Zeal Roselio', 'Zeal Roselio'), ('Drop Holy Pandas', 'Drop Holy Pandas'), ('Cherry MX Green', 'Cherry MX Green'), ('Zeal Zilent', 'Zeal Zilent'), ('Gateron Green', 'Gateron Green')], default='', max_length=50)),
                ('keycaps', models.CharField(blank='False', choices=[('Other', 'Other')], default='', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='', max_length=300)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
            ],
        ),
    ]

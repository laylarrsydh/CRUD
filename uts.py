import imp
from flask import Flask, render_template, url_for, request, redirect, flash
import mysql.connector
application = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port='3306', password='', database='rumahsakit')

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/Signup_UTS', methods=['GET','POST'])
def Signup_UTS():
    print(request.method)
    if request.method == 'GET':
        return render_template('Signup_UTS.html')
    else: 
        request.method == 'POST'
        username = request.form['username']
        password = request.form['password']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO user (username , password) VALUES ('"+username+"','"+password+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('Login_UTS'))

@application.route('/Login_UTS', methods=['GET','POST'])
def Login_UTS():
    print(request.method)
    if request.method == 'GET':
        return render_template('Login_UTS.html')
    else: 
        request.method == 'POST'
        username = request.form['username']
        password = request.form['password']
        db = getMysqlConnection()
        try:
            sqlstr = "SELECT * from user WHERE username='"+username+"'"
            cur = db.cursor()
            cur.execute(sqlstr)
            data = cur.fetchone()
            output_json = cur.fetchall()
            
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        if data == None :            
            return redirect(url_for('Login_UTS'))
        else : 
            if data[1]== password : 
                return render_template('Dashboard_UTS.html')
            else : 
                return redirect(url_for('Login_UTS'))

@application.route('/Dashboard_UTS')
def Dashboard_UTS():
    return render_template('Dashboard_UTS.html')

@application.route('/Registrasi_UTS')
def Registrasi_UTS():
    return render_template('Registrasi_UTS.html')

@application.route('/Perawat_UTS')
def Perawat_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        ID_perawat = request.form['ID_perawat']
        Nama = request.form['Nama']
        Jenis_Kelamin = request.form['Jenis_Kelamin']
        No_Telepon = request.form['No_Telepon']
        try:
            sqlstr = f"insert into perawat (ID_perawat, Nama, Jenis_Kelamin, No_Telepon) values ({ID_perawat}, '{Nama}', '{Jenis_Kelamin}', '{No_Telepon}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM perawat"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('Perawat_UTS.html',data=output_json)

@application.route('/update_perawat/<int:ID_perawat>', methods=['GET', 'POST'])
def update_perawat(ID_perawat):
    db = getMysqlConnection()
    try:
        cur = db.cursor()
        sqlstr = f"SELECT * FROM perawat where ID_perawat = {ID_perawat}"
        cur.execute(sqlstr)
        print('sukses')
        old_data = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)

    try:
        cur = db.cursor()
        sqlstr = f"SELECT ID_perawat FROM perawat"
        cur.execute(sqlstr)
        print('sukses')
        nip = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)

    if request.method == 'GET':
        return render_template('Perawat_UTS.html', data=old_data, ID_perawat=ID_perawat)
    else:
        ID_perawat = request.form['ID_perawat']
        Nama = request.form['Nama']
        Jenis_Kelamin = request.form['Jenis_Kelamin']
        No_Telepon = request.form['No_Telepon']

        if len(Nama) == 0:
            Nama = old_data[0][1]
        if len(Jenis_Kelamin) == 0:
            Jenis_Kelamin = old_data[0][2]
        if len(No_Telepon) == 0:
            No_Telepon = old_data[0][3]

        try:
            cur = db.cursor()
            sqlstr = f"update perawat set Nama='{Nama}', Jenis_Kelamin='{Jenis_Kelamin}', No_Telepon='{No_Telepon}' where ID_perawat={ID_perawat}"
            cur.execute(sqlstr)
            db.commit()
            print('sukses')
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Perawat_UTS'))

@application.route('/delete_perawat/<int:ID_perawat>', methods=['GET', 'POST'])
def delete_perawat(ID_perawat):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM perawat WHERE ID_perawat = '"+str(ID_perawat)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Perawat_UTS'))
    return redirect(url_for('Perawat_UTS'))

@application.route('/Pasien_UTS')
def Pasien_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        ID = request.form['ID']
        Nama = request.form['Nama']
        Tanggal_Lahir = request.form['Tanggal_Lahir']
        Jenis_Kelamin = request.form['Jenis_Kelamin']
        No_Telepon = request.form['No_Telepon']
        Alamat = request.form['Alamat']
        try:
            sqlstr = f"insert into pasien (ID_pasien, Nama, Tanggal_Lahir, Jenis_Kelamin, No_Telepon, Alamat) values ({ID}, '{Nama}', '{Tanggal_Lahir}', '{Jenis_Kelamin}', '{No_Telepon}','{Alamat}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM pasien"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('Pasien_UTS.html',data=output_json)

@application.route('/delete_pasien/<int:ID>', methods=['GET', 'POST'])
def delete_pasien(ID):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM pasien WHERE ID = '"+str(ID)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Pasien_UTS'))
    return redirect(url_for('Pasien_UTS'))

@application.route('/RekamMedis_UTS')
def RekamMedis_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        ID_RM = request.form['ID_RM']
        Tanggal = request.form['Tanggal']
        Keluhan = request.form['Keluhan']
        Pemeriksaan = request.form['Pemeriksaan']
        Pengobatan = request.form['Pengobatan']
        try:
            sqlstr = f"insert into rekammedis (ID_RM, Tanggal, Keluhan, Pemeriksaan, Pengobatan) values ({ID_RM}, '{Tanggal}', '{Keluhan}', '{Pemeriksaan}', '{Pengobatan}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM rekammedis"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('RekamMedis_UTS.html',data=output_json)

@application.route('/delete_rekammedis/<int:ID_RM>', methods=['GET', 'POST'])
def delete_rekammedis(ID_RM):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM rekammedis WHERE ID_RM = '"+str(ID_RM)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('RekamMedis_UTS'))
    return redirect(url_for('RekamMedis_UTS'))

@application.route('/Dokter_UTS')
def Dokter_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        ID_dokter = request.form['ID_dokter']
        Nama = request.form['Nama']
        Spesialis = request.form['Spesialis']
        Jenis_Kelamin = request.form['Jenis_Kelamin']
        No_Telepon = request.form['No_Telepon']
        Alamat = request.form['Alamat']
        try:
            sqlstr = f"insert into dokter (ID_dokter, Nama, Spesialis, Jenis_Kelamin, No_Telepon, Alamat) values ({ID_dokter}, '{Nama}', '{Spesialis}', '{Jenis_Kelamin}', '{No_Telepon}','{Alamat}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM dokter"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('Dokter_UTS.html',data=output_json)

@application.route('/delete_dokter/<int:ID_dokter>', methods=['GET', 'POST'])
def delete_dokter(ID_dokter):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM dokter WHERE ID_dokter = '"+str(ID_dokter)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Dokter_UTS'))
    return redirect(url_for('Dokter_UTS'))

@application.route('/Kamar_UTS')
def Kamar_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        No_Kamar = request.form['No_Kamar']
        Nama = request.form['Nama']
        Jenis = request.form['Jenis']
        Kapasitas = request.form['Kapasitas']
        Fasilitas = request.form['Fasilitas']
        Harga = request.form['Harga']
        try:
            sqlstr = f"insert into kamar (No_Kamar, Nama, Jenis, Kapasitas, Fasilitas, Harga) values ({No_Kamar}, '{Nama}', '{Jenis}', '{Kapasitas}','{Fasilitas}','{Harga}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM kamar"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('Kamar_UTS.html',data=output_json)

@application.route('/delete_kamar/<int:No_Kamar>', methods=['GET', 'POST'])
def delete_kamar(No_Kamar):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM kamar WHERE No_Kamar = '"+str(No_Kamar)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Kamar_UTS'))
    return redirect(url_for('Kamar_UTS'))

@application.route('/Obat_UTS')
def Obat_UTS():
    db = getMysqlConnection()
    if request.method == 'POST':
        Kode_obat = request.form['Kode_obat']
        Nama_obat = request.form['Nama_obat']
        Jenis = request.form['Jenis']
        tahun_produksi = request.form['tahun_produksi']
        masa_berlaku = request.form['masa_berlaku']
        try:
            sqlstr = f"insert into obat (Kode_obat, Nama_obat, Jenis, tahun_produksi, masa_berlaku, Harga) values ({Kode_obat}, '{Nama_obat}', '{Jenis}', '{tahun_produksi}','{masa_berlaku}')"
            cur = db.cursor()
            cur.execute(sqlstr)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        
    try:
        sqlstr = "SELECT * FROM obat"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('Obat_UTS.html',data=output_json)

@application.route('/delete_obat/<int:Kode_obat>', methods=['GET', 'POST'])
def delete_obat(Kode_obat):
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data berhasil ditambahkan."
            sqlstr = "DELETE FROM obat WHERE Kode_obat = '"+str(Kode_obat)+"';"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('Obat_UTS'))
    return redirect(url_for('Obat_UTS'))

if __name__ == '__main__':
    application.run(debug=True)
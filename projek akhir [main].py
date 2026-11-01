from flask import Flask, jsonify, request, render_template  # <-- 1. Tambahkan render_template di sini
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///device_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Database untuk menyimpan data perangkat & pemilik
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    latitude = db.Column(db.Float, default=0.0)
    longitude = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='Offline')

    def to_dict(self):
        return {
            'id': self.id,
            'owner_name': self.owner_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'status': self.status
        }

# Inisialisasi Database
with app.app_context():
    db.create_all()

# ==========================================
# 2. TARUH RUTE HALAMAN UTAMA DI SINI
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')


# Endpoint untuk mendapatkan SEMUA perangkat sekaligus
@app.route('/api/devices', methods=['GET'])
def get_all_devices():
    devices = Device.query.all()
    return jsonify([d.to_dict() for d in devices]), 200

# Endpoint untuk mendaftarkan atau memperbarui data/lokasi perangkat berdasarkan email/nomor HP
@app.route('/api/device', methods=['POST'])
def register_or_update_device():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email wajib diisi'}), 400

    device = Device.query.filter_by(email=email).first()
    
    if not device:
        # Tambah perangkat baru jika email belum terdaftar
        device = Device(
            owner_name=data.get('owner_name', 'Unknown'),
            email=email,
            phone_number=data.get('phone_number', '-'),
            latitude=data.get('latitude', 0.0),
            longitude=data.get('longitude', 0.0),
            status=data.get('status', 'Online')
        )
        db.session.add(device)
    else:
        # Update data perangkat yang sudah ada
        device.owner_name = data.get('owner_name', device.owner_name)
        device.phone_number = data.get('phone_number', device.phone_number)
        device.latitude = data.get('latitude', device.latitude)
        device.longitude = data.get('longitude', device.longitude)
        device.status = data.get('status', device.status)
    
    db.session.commit()
    return jsonify({'message': 'Data perangkat berhasil diperbarui', 'device': device.to_dict()}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from . import db
from datetime import datetime

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codeuai = db.Column(db.String(8))
    titreoperation = db.Column(db.String(255))
    entreprise = db.Column(db.String(255))
    annee_de_livraison = db.Column(db.Integer)
    ville  = db.Column(db.String(255))
    mandataire  = db.Column(db.String(255))
    ppi  = db.Column(db.String(255))
    lycee  = db.Column(db.String(255))
    notification_du_marche = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    etat_d_avancement  = db.Column(db.String(255))
    montant_des_ap_votes_en_meu = db.Column(db.Float)
    cao_attribution  = db.Column(db.DateTime)
    maitrise_d_oeuvre  = db.Column(db.String(255))
    mode_de_devolution  = db.Column(db.String(255))
    annee_d_individualisation = db.Column(db.Integer)
    enveloppe_prev_en_meu = db.Column(db.Float)

    def __repr__(self):
        return '<Investment {}>'.format(self.codeuai) 
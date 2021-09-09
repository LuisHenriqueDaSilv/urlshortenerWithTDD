from flask import request, redirect
import requests

from app import db

#Utils
from .utils import uuid_generator

#Database models
from .database.models import ShortedUrl

class Controller():


    @staticmethod
    def create():
        
        original_url_to_short = request.form.get('url')
        if not original_url_to_short:
            return {
                'status': 'error',
                'message': 'Url to short not provided'
            }, 400

        try:
            requests.get(original_url_to_short)
        except:
            return {
                'status': 'error',
                'message': 'Invalid url'
            }, 400
        
        shorted_url_uuid = uuid_generator(size=6)
        shorted_url = ShortedUrl(
            url=original_url_to_short,
            uuid=shorted_url_uuid
        )
        db.session.add(shorted_url)
        db.session.commit()

        return {
            'status': 'ok',
            'shorted_url_uuid': shorted_url_uuid
        }, 200
        
    @staticmethod
    def read(uuid):

        shorted_url = ShortedUrl.query.filter_by(
            uuid=str(uuid)
        ).first()

        if not shorted_url:
            return {
                'status': 'error',
                'message': 'The requested URL was not found'
            }, 404

        return redirect(shorted_url.url)

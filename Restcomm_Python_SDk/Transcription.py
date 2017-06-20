'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2016, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 '''

import requests
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class TranscriptionList(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/Transcriptions.json'
        r1 = requests.get(Url , auth=(self.Sid, self.AuthToken))

        content = json.loads(r1.text)
        return content

class TranscriptionFilter(object):

    def __init__(self, TranscriptionText, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.text = TranscriptionText

    def FilterText(self):

        params = {'TranscriptionText':self.text}
        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/Transcriptions.json?'
        r2 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r2.text)
        return content

    def FilterPage(self):

        params = {'PageSize' : self.text}
        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Transcriptions.json?'
        r3 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content
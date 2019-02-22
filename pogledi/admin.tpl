% rebase('osnova')
% from datetime import datetime
% format = '%Y-%m-%d'

<h1 class="title">{{ lokacija['naziv'] }}</h1>

<h1 class="title">Rezervacije<h1>
<form action="/izposodi" method="post">
<table class="table is-striped">
    <thead>
        <tr>
            <th>Od</th>
            <th>Do</th>
            <th>Ime</td>
            <th>Priimek</td>
            <th>Številka osebne izkaznice</th>
            <th>Znamka</th>
            <th>Model</th>
            <th>Serijska številka</th>
            <th>Lokacija kolesa</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
% datum = datetime.now()
% for r in rezervacije:
<tr>
    % datum_rezervacije = datetime.strptime(r['datum_od'], format)
    % od = datum_rezervacije.strftime('%d.%m.%Y')
    % do = datetime.strptime(r['datum_do'], format).strftime('%d.%m.%Y')
    <td>{{ od }}</td>
    <td>{{ do }}</td>
    <td>{{ r['ime'] }}</td>
    <td>{{ r['priimek'] }}</td>
    <td>{{ r['stevilka_osebne'] }}</td>
    <td>{{ r['znamka'] }}</td>
    <td>{{ r['model'] }}</td>
    <td>{{ r['serijska_stevilka'] }}</td>
    <td>{{ r['naziv'] }}</td>
    <td>
    % if lokacija['id'] != r['lokacija']:
        <button class="button" name="prestavi" value="{{ r['kolo'] }}">Prestavi</button>
    % elif datum_rezervacije <= datum:
        <button class="button" name="izposodi" value="{{ r['id'] }}">Izposodi</button>
    % end
    </td>
</tr>
% end
    </tbody>
</table>
</form>

<br>
<h1 class="title">Izposoje</h1>
<form action="/izposodi" method="post">
<table class="table is-striped">
    <thead>
        <tr>
            <th>Od</th>
            <th>Do</th>
            <th>Ime</td>
            <th>Priimek</td>
            <th>Številka osebne izkaznice</th>
            <th>Znamka</th>
            <th>Model</th>
            <th>Serijska številka</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
% for i in izposoje:
<tr>
    % od = datetime.strptime(i['datum_od'], format).strftime('%d.%m.%Y')
    % do = datetime.strptime(i['datum_do'], format).strftime('%d.%m.%Y')
    <td>{{ od }}</td>
    <td>{{ do }}</td>
    <td>{{ i['ime'] }}</td>
    <td>{{ i['priimek'] }}</td>
    <td>{{ i['stevilka_osebne'] }}</td>
    <td>{{ i['znamka'] }}</td>
    <td>{{ i['model'] }}</td>
    <td>{{ i['serijska_stevilka'] }}</td>
    <td>
        <button class="button" name="vrni" value="{{ i['id'] }}">Vrni</button>
    </td>
</tr>
% end
    </tbody>
</table>
</form>

<br>

<div class="columns">
<div class="column"><form action="/odjava"><button class="button"">Odjava</button></form></div>
<div class="column"><form action="/statistika"><button class="button"">Statistika</button></form></div>
<div>
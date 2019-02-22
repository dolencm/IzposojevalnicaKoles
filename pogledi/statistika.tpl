% rebase('osnova')

<h1 class="title">Zaključene izposoje</h1>

<table class="table is-striped">
    <thead>
        <tr>
            <th>Od</th>
            <th>Do</th>
            <th>Ime</td>
            <th>Priimek</td>
            <th>Znamka</th>
            <th>Model</th>
        </tr>
    </thead>
    <tbody>
% for vrstica in podatki:
<tr>
    <td>{{ vrstica['datum_od'] }}</td>
    <td>{{ vrstica['datum_do'] }}</td>
    <td>{{ vrstica['ime'] }}</td>
    <td>{{ vrstica['priimek'] }}</td>
    <td>{{ vrstica['znamka'] }}</td>
    <td>{{ vrstica['model'] }}</td>
</tr>
% end
</tbody>
</table>

<form action="/admin"><button class="button is-primary">Nazaj</button></form>
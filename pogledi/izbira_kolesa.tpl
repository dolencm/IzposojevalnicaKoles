% rebase('osnova')

% if kolesa == None:
<h1 class="title">Žal v željenem obdobju nimamo na voljo prostih koles</h1>
% else:

<h1 class="title">Katero kolo želite?</h1>
<table class="table is-striped">
    <thead>
        <tr>
            <th>Znamka</th>
            <th>Model</th>
            <th>Tip</th>
            <th>Velikost</th>
            <th>Slika</th>
            <th></td>
        </tr>
    </thead>
    <tbody>

    <form action="/rezervacija" method="post">
% for kolo in kolesa:
<tr>
    <td>{{ kolo['znamka'] }}</td>
    <td>{{ kolo['model'] }}</td>
    <td>{{ kolo['tip'] }}</td>
    <td>{{ kolo['velikost'] }}</td>
    <td><figure class="image"><img src="slike/{{ kolo['slika'] }}"></figure></td>
    <td>
        <button type="submit" name="kolo" class="button is-primary" value="{{ kolo['id'] }}">Izberi!</button>
    </td>
</tr>
% end
        </form>
    </tbody>
</table>

% end
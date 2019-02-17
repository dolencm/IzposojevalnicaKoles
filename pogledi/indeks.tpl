% rebase('osnova')

<h1 class="title">Pozdravljeni! Kje želite kolesariti?</h1>

<div class="columns">
% for lokacija in lokacije:
    <div class="column">
        <p>{{ lokacija['naslov'] }}</p>
        <p>{{ lokacija['posta'] }} {{ lokacija['kraj'] }}</p>
        <iframe width="450" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/maps?ll={{ lokacija['zemljepisna_sirina'] }},{{ lokacija['zemljepisna_dolzina'] }}&z=15&output=embed"></iframe>
        <p>
            <form action="/izbira_kolesa" method="post">
                <input type="hidden" name="lokacija" value="{{ lokacija['id'] }}"/>
                <button type="submit" class="button is-primary">Tukaj!</button>
            </form>
        </p>
    </div>
% end
</div>
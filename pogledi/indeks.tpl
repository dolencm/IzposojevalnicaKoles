% rebase('osnova')

<h1 class="title">Pozdravljeni!</h1>

<h1 class="title">Kdaj želite kolo?</h1>

<input type="date" name="datum" data-display-mode="inline"/>
<script>
let calendars = bulmaCalendar.attach('[type="date"]', {
    dateFormat: 'DD.MM.YYYY',
    isRange: true,
    showHeader: false,
    minDate: new Date({{ minDate }})
});

calendars.on('select', function(dat) {
    document.getElementById("datum_od").value = dat.data.start.toISOString();
    document.getElementById("datum_do").value = dat.data.end.toISOString();
});
</script>
<br>
<h1 class="title">Kje želite kolesariti?</h1>

<div class="columns">
% for lokacija in lokacije:
    <div class="column">
        <p>{{ lokacija['naslov'] }}</p>
        <p>{{ lokacija['posta'] }} {{ lokacija['kraj'] }}</p>
        <iframe width="450" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/maps?ll={{ lokacija['zemljepisna_sirina'] }},{{ lokacija['zemljepisna_dolzina'] }}&z=15&output=embed"></iframe>
        <p>
            <form action="/izbira_kolesa" method="post">
                <input type="hidden" name="lokacija" value="{{ lokacija['id'] }}"/>
                <input type="hidden" name="datum_od" id="datum_od"/>
                <input type="hidden" name="datum_do" id="datum_do"/>
                <button type="submit" class="button is-primary">Tukaj!</button>
            </form>
        </p>
    </div>
% end
</div>
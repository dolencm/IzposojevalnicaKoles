% rebase('osnova')

<h1 class="title">Pozdravljeni!</h1>

<div class="columns">
% if uporabnik != None:
<div class="column"><h1 class="subtitle">{{ uporabnik['ime'] }} {{ uporabnik['priimek'] }}</h1></div>
<div class="column"><form action="/odjava"><button class="button">Odjava</button></form></div>
% else:
<div class="column"><form action="/prijava"><button class="button">Prijava</button></form></div>
<div class="column"><form action="/registracija"><button class="button">Registracija</button></form></div>
% end
</div>

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
    let d_od = dat.data.start;
    let d_do = dat.data.end;
    document.getElementById("datum_od").value = d_od.getFullYear() + '-' + (d_od.getMonth() + 1) + '-' + d_od.getDate();
    document.getElementById("datum_do").value = d_do.getFullYear() + '-' + (d_do.getMonth() + 1) + '-' + d_do.getDate();
});
</script>
<br>
<h1 class="title">Kje želite kolesariti?</h1>

<form action="/izbira_kolesa" method="post">
<input type="hidden" name="datum_od" id="datum_od"/>
<input type="hidden" name="datum_do" id="datum_do"/>
<div class="columns">
% for lokacija in lokacije:
    <div class="column">
        <p>{{ lokacija['naslov'] }}</p>
        <p>{{ lokacija['posta'] }} {{ lokacija['kraj'] }}</p>
        <iframe width="450" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/maps?ll={{ lokacija['zemljepisna_sirina'] }},{{ lokacija['zemljepisna_dolzina'] }}&z=15&output=embed"></iframe>
        <p>
            <button type="submit" name="lokacija" class="button" value="{{ lokacija['id'] }}">Tukaj!</button>
        </p>
    </div>
% end
</div>
</form>
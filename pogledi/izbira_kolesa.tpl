% rebase('osnova')

<script>
const calendars = bulmaCalendar.attach('[type="date"]', {});
console.log(bulmaCalendar);
</script>
<h1 class="title">Izbira kolesa</h1>

<input type="date" name="datum_od" data-display-mode="inline"/>

<input type="file" accept="image/png, image/jpeg"/>

<p>
<img src="slike/900_pro.jpg">
</p>

% for kolo in kolesa:
<p>{{ kolo['znamka'] }} {{ kolo['tip'] }}</h1>
% end
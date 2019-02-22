% rebase('osnova')

% if napaka != None:
<h1 class="title">Napaka!</h1>
<h1 class="subtitle has-text-danger">{{ napaka }}</h1>
<br>
% end

<h1 class="title">Registracija novega uporabnika</h1>

<div class="columns">
    <form action="/registracija" method="post">
        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Ime</label>
            </div>
            <div class="field">
                <input class="input" type="text" name="ime"/>
            </div>
        </div>
        
        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Priimek</label>
            </div>
            <div class="field">
                <input class="input" type="text" name="priimek"/>
            </div>
        </div>
        
        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Uporabniško ime</label>
            </div>
            <div class="field">
                <input class="input" type="text" name="uporabnisko_ime"/>
            </div>
        </div>

        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Geslo</label>
            </div>
            <div class="field">
                <input class="input" type="password" name="geslo"/>
            </div>
        </div>

        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Ponovi geslo</label>
            </div>
            <div class="field">
                <input class="input" type="password" name="potrditev"/>
            </div>
        </div>

        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">E-Mail</label>
            </div>
            <div class="field">
                <input class="input" type="email" name="email"/>
            </div>
        </div>

        <div class="field is-horizontal">
            <div class="field-label">
                <label class="label">Številka osebne izkaznice</label>
            </div>
            <div class="field">
                <input class="input" type="text" name="stevilka_osebne"/>
            </div>
        </div>

        <div class="field is-horizontal">
            <div class="field-label"/>
            <div class="field">
                <button type="submit" class="button is-primary">Registracija</button>
            </div>
    </form>
</div>
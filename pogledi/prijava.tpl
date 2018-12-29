% rebase('osnova')

<h1 class="title">Prijavi se v sistem</h1>

<div class="columns">
    <form action="/prijava" method="post">
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
            <div class="field-label"/>
            <div class="field">
                <button type="submit" class="button is-primary">Prijava</button>
            </div>
        </div>
    </form>
</div>
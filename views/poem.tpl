% rebase("layout.tpl", title="Pastiche", year=year)

<div class="jumbotron">
    <br>
    <br>
    % for line in poem:
        <p class="lead">
            {{line.capitalize()}}
        </p>
    %end
</div>
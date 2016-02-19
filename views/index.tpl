% rebase("layout.tpl", title="Pastiche", year=year)



<div class="jumbotron">
    <h1>Speak, Memory...</h1>
    <p class="lead">"O soul, we have positively gain'd a hearing, to far more than the gown of orchids in the wind, a few light kisses, a few well held hands to hasten holding."</p>
    <p>-- Pastiche</p>
</div>
<div>
    <h2>Start your masterpiece</h2>
    <p>
        Pastiche generates original poetry inspired by the greats. Select
        your favorite poets, a poetic form, rhyme scheme, and length, 
        or let Pastiche choose for you. Then, viola -- an instant,
        original masterpiece!
    </p>
    <p>
        Use Pastiche for fun, inspiration, or maybe even stumble upon 
        the world's next greatest work of literary genius.
    </p>
</div>
<br>
<br>

<form action="/" method="post" name="userSelection">
    <div class="row">
        <div class="col-md-5">
            <div class="panel panel-default">
                <div class="panel-heading">1. Choose your inspiration</div>
                <div class="panel-body">

                    %for poet in poets:
                    <div class="col-lg-6">
                        <div class="input-group1">
                            <input type="checkbox"
                                   class="authors"
                                   onclick="notRandom()"
                                   name={{poet}}>&nbsp;&nbsp;{{poet}}
                        </div>
                    </div>
                    <br>
                    %end
                    <div class="col-lg-6">
                        <div class="input-group1">
                            <input type="checkbox"
                                   class="authors"
                                   id="Random"
                                   onclick="randomAuthors()"
                                   name=Random>&nbsp;&nbsp;Random
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-5">
                <div class="panel panel-default">
                    <div class="panel-heading">2. Choose your rhyme scheme and length:</div>
                    <div class="panel-body" id="forms">
                        <div class="col-lg-6">
                            <div class="input-group">
                                <input type="checkbox"
                                       class="poeticForms"
                                       id="AABBBox"
                                       name="pf_AABB">&nbsp;&nbsp;AABB
                            </div>
                        </div>
                        <br>
                        <fieldset class="form-group"
                                  style="visibility: hidden;
                                     display: inline-block;"
                                  id="selectLinesAABB">
                            <label for="exampleSelect1">Choose number of lines:</label>
                            <select class="form-control" name="nL_AABB" id="exampleSelect1">
                                <option>2</option>
                                <option>4</option>
                                <option>6</option>
                            </select>
                        </fieldset>
                        <br>
                        <div class="col-lg-6" style="display: inline-block;">
                            <div class="input-group">
                                <input type="checkbox"
                                       class="poeticForms"
                                       id="ABABBox"
                                       name="pf_ABAB">&nbsp;&nbsp;ABAB
                            </div>
                        </div>
                        <br>
                        <fieldset class="form-group"
                                  style="visibility: hidden;
                                     display: inline-block;"
                                  id="selectLinesABAB">
                            <label for="exampleSelect1">Choose number of lines:</label>
                            <select class="form-control" name="nL_ABAB" id="exampleSelect1">
                                <option>2</option>
                                <option>4</option>
                                <option>6</option>
                            </select>
                        </fieldset>
                        <br>
                        <div class="col-lg-6">
                            <div class="input-group">
                                <input type="checkbox"
                                       class="poeticForms"
                                       name="pf_Random">&nbsp;&nbsp;Random
                            </div>
                        </div>
                        <br>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <button type="submit" 
            class="btn-btn-primary-outline"
            onclick="loading()">Compose</button>
</form>

<p>
    <div id="loading_message"></div>
</p>



  
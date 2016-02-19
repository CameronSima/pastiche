% rebase('layout.tpl', title='Poems', year=year)

%for poem in poems:
        <div class="date">
            {{poem[1]}}
        </div>
        <div class="likes">
            <a class="clickable" onclick="vote({{poem[0]}}, 'up')">like</a> /<a class="clickable"  onclick="vote({{poem[0]}}, 'down')"> dislike
            </a> 
            <div id="count{{poem[0]}}" class="unvoted">
                Likes: {{poem[3]}}
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-body"> 
                % for i in range(len(poem[2].split('^^'))):
                    <p>{{poem[2].split('^^')[i]}}</p>
                % end                 
            </div>
        </div>
    
%end
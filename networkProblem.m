%###############################
%######  Nikoleta Chantzi ######
%#####  Network Component  #####
%#### FinalProject|ENGS103  ####
%###############################
%% Prim's Algorithm
% Step 1
distances = csvread("Network Problem-PivotTable.csv");
M = 10^6;
% Step 2
curTreeNodes= [1]; % Represents the set of nodes in the current tree 
curTree=[]; % Represents  the  set  of  arcs  in the  current  tree.  
            % Each  row  will  have  2  values  i  and  j  which  are the  two 
            % end-nodes of that arc 
% Step 3
while length(curTreeNodes)<length(distances)
                curRows = distances*M;
                % Now  only  for those  rows  in  D that 
                % correspond  to  current tree  nodes,  divide  each  element  by  M.
                for k = curTreeNodes
                    for l = 1:18
                        curRows(k,l) = curRows(k,l)*(1/M); 
                    end 
                end
                % Step 4
                % Still inside the loop, 
                % set all values in all columns of  curRows that represent the tree nodes to M. 
                for m = curTreeNodes
                    for n = 1:18
                        curRows(n,m) = M;
                    end 
                end         
                % Step 5
                % val  stores  the  minimum  value  in curRows and ind stores the location of this minimum
                [val,ind]=min(curRows(:)); 
                %The next two lines are used to get the row and column number 
                % of this minimum value in the original matrix curRows.  
                c=ceil(ind/size(curRows,1));
                r=ind-(c-1)*size(curRows,1);
                % append  the  newly  found arc  and  node  to  the  curTree and  
                % curTreeNodes  matrices  respectively  and end the loop
                curTree = [curTree;[r,c]];
                curTreeNodes = [curTreeNodes;c];
end
% Step 6
curTree % contains MST solution

finalCost = 0;
for i= 1:length(curTree)
    finalCost = finalCost + distances(curTree(i,1),curTree(i,2));
end
finalCost % contains cost of MST solution

%% Dijkstra's Algorithm
% Data Structures
startingPoint = 14;
dist = csvread("Network Problem-WithoutIAD.csv");
incid = csvread("Network Problem-WithoutIAD.csv");
incid(incid>0) = 1;
% Initial Conditions
inf=sum(sum(dist));
d=ones(1,18)*inf; d(startingPoint)=0;
p=zeros(1,18);
k=startingPoint;
closed=zeros(1,18); closed(1)=1;
%Writing the Steps within each Iteration
while (sum(closed)<18)
    %Update
    for j=1:18
        if (incid(k,j)==1)
            if (d(j)>d(k)+dist(k,j))
                d(j)=d(k)+dist(k,j);
                p(j)=k;
            end
        end
    end
    %Closure
    [minval minloc]=min(d+closed*inf);
    closed(minloc)=1;
    %Terminate
    k=minloc;
end
%Exiting the Loop and Post-Processing
for i=1:18
    if i ~= startingPoint
        path=i;
        j=i;
        while (p(j)~= startingPoint)
            path(length(path)+1)=p(j);
            j=p(j);
        end
        l=length(path);
        finalpath=zeros(1,l);
        for j=1:length(path)
            finalpath(l-j+1)=path(j);
        end
        i
        finalpath      
    end
end
d % contains shortest path from ATH to all different destinations (including LHR and EDI)
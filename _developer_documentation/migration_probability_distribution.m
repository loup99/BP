majority_cutoff = 10;
large_minority_cutoff = 25;
small_minority_cutoff = 100;

%These curves weight the underlying 12:6:3:1 distribution based on development, 
%with a specfic cutoff (and above) becoming a 0% probability.
probability_nothing = @(x) max(x./10,0.0);
probability_something = @(x,cutoff) max((-1./cutoff)*x+1,0);
development = 0:1:100;

probability_distribution = ...
[60.*probability_nothing(development);...
 30.*probability_something(development,small_minority_cutoff);...
 15.*probability_something(development,large_minority_cutoff);...
 05.*probability_something(development,majority_cutoff);];
 
#Normalize probability_distribution
probability_distribution = 100.*probability_distribution./repmat(sum(probability_distribution,1),4,1);

figure(1);
clf(1);
hold on;
%Actual Curves
plot(development,probability_distribution(1,:),'k-');
plot(development,probability_distribution(2,:),'g-');
plot(development,probability_distribution(3,:),'r-');
plot(development,probability_distribution(4,:),'b-');
%Cutoffs
plot(small_minority_cutoff.*ones(1,101),linspace(0,100,101),'g:','LineWidth',2.00);
plot(large_minority_cutoff.*ones(1,101),linspace(0,100,101),'r:','LineWidth',2.00);
plot(majority_cutoff.*ones(1,101),linspace(0,100,101),'b:','LineWidth',2.00);
hold off;
axis([0,100,0,100]);
grid on;
set(gca,'XTick',0:10:100,'YTick',0:10:100);
xlabel('Development');
ylabel('Probability (%)');
title('Development Effect on Migration Events');

legend(...
'Probability Nothing',...
'Probability Small Minority',...
'Probability Large Minority',...
'Probability Majority Population',...
'Small Minority Cutoff',...
'Large Minority Cutoff',...
'Majority Population Cutoff',...
'Location','EastOutside');

#! /usr/bin/perl -w
BEGIN {push (@INC, "/home/sciminer/ANNOTATION/SciMinerDB/Modules/");}

use lib '/Users/ozgedincsoy/Documents/School/spring19/seniorproject/genes';
no warnings "experimental::declared_refs";
use Sciminer;
use feature "declared_refs";
 use feature "refaliasing";
use strict; use warnings;

my $filename = 'commonIds.txt';
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

#my ($fetchStatus, $fetched, $count, \@pmids) = &search_entrez_with_pubmed_query("\"Amyotrophic lateral sclerosis\"[MeSH] AND \"Reactive Oxygen Species\"[MeSH]");
#combination of autism and epilepsy
#my ($fetchStatus, $fetched, $count, \@pmids) = &search_entrez_with_pubmed_query("(\"Autism\"[ALL] OR \"Autism Spectrum Disorder\"[ALL] OR \"Epilepsy\"[ALL] OR (\"Malformations of\"[ALL] AND (\"cortical\"[ALL] OR \"cerebral\"[ALL] OR \"cerebellar\"[ALL]) AND \"development\"[ALL]) OR \"Intellectual Disability\"[ALL] OR \"Mental Retardation\"[ALL] OR \"Cognition Deficits\"[ALL] OR \"dendrite branching\"[ALL])");
#just autism
#my ($fetchStatus, $fetched, $count, \@pmids) = &search_entrez_with_pubmed_query("(\"Autism\"[ALL] OR \"Autism Spectrum Disorder\"[ALL]");
#just epilepsy
#my ($fetchStatus, $fetched, $count, \@pmids) = &search_entrez_with_pubmed_query("(\"Epilepsy\"[ALL] OR (\"Malformations of\"[ALL] AND (\"cortical\"[ALL] OR \"cerebral\"[ALL] OR \"cerebellar\"[ALL]) AND \"development\"[ALL]) OR \"Intellectual Disability\"[ALL] OR \"Mental Retardation\"[ALL] OR \"Cognition Deficits\"[ALL] OR \"dendrite branching\"[ALL])");
#common in autism and epilepsy
my ($fetchStatus, $fetched, $count, \@pmids) = &search_entrez_with_pubmed_query("((\"Autism\"[ALL] OR \"Autism Spectrum Disorder\"[ALL]) AND (\"Epilepsy\"[ALL] OR (\"Malformations of\"[ALL] AND (\"cortical\"[ALL] OR \"cerebral\"[ALL] OR \"cerebellar\"[ALL]) AND \"development\"[ALL]) OR \"Intellectual Disability\"[ALL] OR \"Mental Retardation\"[ALL] OR \"Cognition Deficits\"[ALL] OR \"dendrite branching\"[ALL]))");

for my $var (@pmids){
	print $fh ($var . "\n");
}

print($count);
close $fh;

exit;

#"Autism"[ALL] OR "Autism Spectrum Disorder"[ALL] OR "Epilepsy"[ALL] OR ("Malformations of"[ALL] AND ("cortical"[ALL] OR "cerebral"[ALL] OR "cerebellar"[ALL]) AND "development"[ALL]) OR "Intellectual Disability"[ALL] OR "Mental Retardation"[ALL] OR "Cognition Deficits"[ALL] OR "dendrite branching"[ALL]

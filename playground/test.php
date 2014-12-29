<?php


$_POST = array
(
    '_wpnonce' => 'ea2ea63b9e',
    '_wp_http_referer' => '/wp-admin/post.php?post=5145&action=edit&message=1',
    'user_ID' => 1,
    'action' => 'editpost',
    'originalaction' => 'editpost',
    'post_author' => 1,
    'post_type' => 'wpsc_cart_orders',
    'original_post_status' => 'publish',
    'referredby' => 'http://thenoticeca.pangia.org/wp-admin/post.php?post=5145&action=edit',
    '_wp_original_http_referer' => 'http://thenoticeca.pangia.org/wp-admin/post.php?post=5145&action=edit',
    'post_ID' => 5145,
    'autosavenonce' => '268993b4c1',
    'meta-box-order-nonce' => '0119377e5d',
    'closedpostboxesnonce' => 'cf2d885322',
    'wp-preview' => '',
    'hidden_post_status' => 'publish',
    'post_status' => 'publish',
    'hidden_post_password' => '',
    'hidden_post_visibility' => 'public',
    'visibility' => 'public',
    'post_password' => '',
    'mm' => '04',
    'jj' => '23',
    'aa' => '2014',
    'hh' => '17',
    'mn' => '00',
    'ss' => '34',
    'hidden_mm' => '04',
    'cur_mm' => '04',
    'hidden_jj' => '23',
    'cur_jj' => '26',
    'hidden_aa' => '2014',
    'cur_aa' => '2014',
    'hidden_hh' => '17',
    'cur_hh' => '19',
    'hidden_mn' => '00',
    'cur_mn' => '29',
    'original_publish' => 'Update',
    'save' => 'Update',
    'wpsc_first_name' => 'Elijah',
    'wpsc_last_name' => 'Ethun',
    'wpsc_email_address' => 'yarhajile@gmail.com',
    'wpsc_ipaddress' => '97.115.166.155',
    'wpsc_total_amount' => '292.00',
    'wpsc_address' => '1 Main St, San Jose, CA, 95131, United States',
    'wpsc_buyer_email_sent' => 'Yes. Email sent to: yarhajile@gmail.com',
    'wpsc_applied_coupon' => '',
    'wpsc_order_status' => 'Submitted (paid)',
    'wpsc_comments' => '',
    'thenotice_0_dba_form' => 'legal_notice',
    'thenotice_0_total' => '130.00',
    'thenotice_0_county' => 'Los Angeles',
    'thenotice_0_city' => 'San Fran Angeles',
    'thenotice_0_type_of_legal_notice' => 'Notice of Auto Lien Sale',
    'thenotice_0_run_notice_duration' => 4,
    'thenotice_0_publication_start_date' => '04-25-2014',
    'thenotice_0_publication_end_date' => '05-23-2014',
    'thenotice_0_title' => 'Two line
title text',
    'thenotice_0_notice_text' => 'Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print
Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print
Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print',

    'thenotice_1_dba_form' => 'legal_notice',
    'thenotice_1_total' => '162.00',
    'thenotice_1_county' => 'Los Angeles',
    'thenotice_1_city' => 'Los Angeles',
    'thenotice_1_type_of_legal_notice' => 'Probate Sale of Real Property',
    'thenotice_1_run_notice_duration' => 3,
    'thenotice_1_publication_start_date' => '04-25-2014',
    'thenotice_1_publication_end_date' => '05-16-2014',
    'thenotice_1_title' => 'Some other title
is also 2 lines long',
    'thenotice_1_notice_text' => 'Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print
Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print
Select the County that you need to publish your Le
gal Notice in.
*Take note that The Notice is a weekly paper. If y
ou are required to run your notice for 4 times, th
at would equate to 4 weeks in our print
ERE',
    'post_name' => 'wpsc-cart-order-25',
    'post_mime_type' => '',
    'ID' => 5145,
    'comment_status' => 'closed',
    'ping_status' => 'closed'
);


$dba_form = array( );

if ( $matches = preg_grep( "/^thenotice_/i", array_keys( $_POST ) ) )
{
    foreach( $matches as $match )
    {
       $index	= substr( $match, 10, 1 );
       $key	= substr( $match, 12, strlen( $match ) );
       $value	= $_POST[$match];


       $dba_form[$index][$key] = $value;       
#       echo $index . "\n";
#       echo $key . "\n";
#       echo $value . "\n";
#       echo "-------\n";
    }
}


print_r($dba_form);
